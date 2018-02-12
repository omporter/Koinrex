from django.db import models
from django.http import JsonResponse
from koinrex.users.models import User
from moneybag.wrappers.litecoin import LTCKey
from moneybag.wrappers.coinbin import convert, convert_usd, get_btc_value
from moneybag.wrappers.blockcypher import address_current_transactions as act
from moneybag.wrappers.blockcypher import address_current_balance as acb
from moneybag.wrappers.blockcypher import address_received as a_rec
from moneybag.wrappers.blockcypher import address_sent as a_sent


from bit import Key

# Import for converting float to decimal in AddressABC

import decimal

from django_rq import job

# TODO 1 = Change precision in decimal return value in get_btc_value()
# TODO 2 = Make code more DRY in fetch from blockchain methods
# TODO 3 = Move transactions to its own app


class AddressABC(models.Model):
    """
    Description: Abstract base class for Cryptocoin Address model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    sec_key = models.CharField(
        max_length=128, unique=True, editable=False)
    pub_key = models.CharField(
        max_length=64, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    transaction_count = models.IntegerField(default=0)
    balance = models.DecimalField(
        max_digits=32, decimal_places=8, default=0.00000001)
    amount_received = models.DecimalField(
        max_digits=32, decimal_places=8, default=0.00000001)
    amount_sent = models.DecimalField(
        max_digits=32, decimal_places=8, default=0.00000001)

    # Returns JSON for user's coins and their corresponding balances
    @classmethod
    def get_all_balance(cls, user_id):
        total = {}
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            total.update({str(user_object.pub_key): {'user_email': str(user_object.user.email),
                                                     'user_coin': str(user_object.currency_name),
                                                     'user_balance': user_object.balance,
                                                     'currency_ticker': user_object.currency_ticker,
                                                     'coin_btc_value': get_btc_value(user_object.balance,user_object.currency_ticker)}})
        return JsonResponse(total)

    # Returns JSON of coin name with its corresponding unique address
    # instances of a given user
    @classmethod
    def get_user_moneybag(cls, user_id):
        moneybag = {}
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            moneybag.update({str(user_object.currency_name)
                            : str(user_object.pub_key)})
        return JsonResponse(moneybag)


    # TODO 1 = make return value precision to 8 decimal places

    @classmethod
    def get_total_btc_value(cls, user_id):
        btc_val = 0
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            # If ticker == BTC then convert value and add to current balance
            if user_object.currency_ticker == 'BTC':
                btc_val += user_object.balance
            else:
                btc_val += (user_object.balance *
                            decimal.Decimal(convert(user_object.currency_ticker, 'BTC')))
        return btc_val


    # Returns a user's total USD balance converted with Coinbin API
    @classmethod
    def get_usd_value(cls, user_id):
        current_usd_value = 0
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            current_usd_value += decimal.Decimal(convert_usd(
                user_object.currency_ticker, user_object.balance))
        return current_usd_value

    """
    Methods below are to be wrapped in a queue
    """

    # TODO 2 = Refactor code below to reduce code copypasta! (Use classes)

    # Fetches all current transactions from blockchain for all addresses of a
    # given user and returns a dictionary of updated items
    @classmethod
    @job('default')
    def fetch_tx_count(cls, user_id):
        updated = dict()
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            address = str(user_object.pub_key)
            ticker = str(user_object.currency_ticker).lower()
            current_tx_count = act(address, ticker)
            user_object.transaction_count = current_tx_count
            user_object.save()
            updated.update(
                {user_object: {'email': user_object.user.email,
                               'coin': ticker,
                               'address': address,
                               'updated_tx_count': user_object.transaction_count}})
        return updated

    # Fetches all current balances from blockchain for all addresses of a
    # given user and returns a dictionary of updated items
    @classmethod
    @job('default')
    def fetch_balance(cls, user_id):
        updated = dict()
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            address = str(user_object.pub_key)
            ticker = str(user_object.currency_ticker).lower()
            current_balance = acb(address, ticker)
            user_object.balance = current_balance
            user_object.save()
            updated.update(
                {user_object: {'email': user_object.user.email,
                               'coin': ticker,
                               'address': address,
                               'updated_balance': user_object.balance}})
        return updated

    # Fetches all amount received's from blockchain for all addresses of a
    # given user and returns a dictionary of updated items
    @classmethod
    @job('default')
    def fetch_amt_received(cls, user_id):
        updated = dict()
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            address = str(user_object.pub_key)
            ticker = str(user_object.currency_ticker).lower()
            current_received = a_rec(address, ticker)
            user_object.amount_received = current_received
            user_object.save()
            updated.update(
                {user_object: {'email': user_object.user.email,
                               'coin': ticker,
                               'address': address,
                               'updated_amt_received': user_object.amount_received}})
        return updated

    # Fetches all amount sent's from blockchain for all addresses of a
    # given user and returns a dictionary of updated items
    @classmethod
    @job('default')
    def fetch_amt_sent(cls, user_id):
        updated = dict()
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            address = str(user_object.pub_key)
            ticker = str(user_object.currency_ticker).lower()
            current_sent = a_sent(address, ticker)
            user_object.amount_sent = current_sent
            user_object.save()
            updated.update(
                {user_object: {'email': user_object.user.email,
                               'coin': ticker,
                               'address': address,
                               'updated_amt_sent': user_object.amount_sent}})
        return updated

    class Meta:
        abstract = True


class CurrencyABC(models.Model):
    """
    Abstract base class for Cryptocoin Currency model
    """
    currency_name = models.CharField(max_length=32, editable=False)
    currency_ticker = models.CharField(max_length=16, editable=False)
    currency_min_div_unit = models.DecimalField(
        max_digits=12, decimal_places=12, editable=False)
    currency_symbol = models.CharField(max_length=2, null=True, editable=False)

    # Returns all the coins in the Koinrex universe
    @classmethod
    def get_list_of_coins(cls):
        coin_dict = dict()
        coin_name_list = list()
        coin_ticker_list = list()
        for coins in cls.__subclasses__():
            # FIXME = Hardcoded first element to query only the first instance of that Currency class       
            coin_name_list.append(coins.objects.get(id=1).currency_name)
            coin_ticker_list.append(coins.objects.get(id=1).currency_ticker)
        payload = {'coin_list': coin_name_list, 
                   'coin_ticker': coin_ticker_list}
        coin_dict.update(payload)
        return JsonResponse(coin_dict)

    class Meta:
        abstract = True


class BitcoinAddress(AddressABC, CurrencyABC):
    """
    Bitcoin Address model which stores and generates the pub/sec key pair
    """

    def __init__(self, *args, **kwargs):
        super(BitcoinAddress, self).__init__(*args, **kwargs)
        if self.sec_key == '' and self.pub_key == '':
            # if nothing is there, create, convert and set
            self.sec_key = str(Key().to_hex())
            self.pub_key = str(Key.from_hex(self.sec_key).address)

            # Set the currency specific details
            self.currency_min_div_unit = 0.00000001
            self.currency_name = 'Bitcoin'
            self.currency_ticker = 'BTC'
            self.currency_symbol = '₿'

    def key_object(self):
        # returns Key object
        return Key.from_hex(self.sec_key)

    def wif(self):
        # returns priv. key only as a string (WIF)
        return self.key_object().to_wif()

    def __str__(self):
        return self.pub_key

    class Meta:
        verbose_name = 'Bitcoin Address'
        verbose_name_plural = 'Bitcoin Addresses'


class LitecoinAddress(AddressABC, CurrencyABC):
    """
    Litecoin Address model which stores and generates the pub/sec key pair
    """

    def __init__(self, *args, **kwargs):
        super(LitecoinAddress, self).__init__(*args, **kwargs)
        if self.sec_key == '' and self.pub_key == '':
            # if nothing is there, create, convert and set
            pair = LTCKey()
            self.sec_key = str(pair.keyval()['sec_key'])
            self.pub_key = str(pair.keyval()['pub_key'])
            self.currency_min_div_unit = 0.00000001
            self.currency_name = 'Litecoin'
            self.currency_ticker = 'LTC'
            self.currency_symbol = 'Ł'

    def key_object(self):
        return (self.sec_key, self.pub_key)

    def __str__(self):
        return self.pub_key

    class Meta:
        verbose_name = 'Litecoin Address'
        verbose_name_plural = 'Litecoin Addresses'
