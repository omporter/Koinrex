"""

Changes in AddressABC : Convert BTC to USD till the end of class

Changes in CurrencyABC : added a new function get_list_of_coins 

Need to work on transactions now

"""

from django.db import models

from koinrex.users.models import User
from moneybag.wrappers.litecoin import LTCKey
from moneybag.wrappers.coinbin import convert,convert_usd

from bit import Key

# Import for converting float to decimal in AddressABC

import decimal
import json
# Create your models here.


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
    transaction_count = models.IntegerField()
    balance = models.DecimalField(max_digits=32, decimal_places=8)
    amount_in = models.DecimalField(max_digits=32, decimal_places=8)
    amount_out = models.DecimalField(max_digits=32, decimal_places=8)
    # TODO add trading balance

    @classmethod  # TODO modify to return a dictionary of values against its corresponding coin
    def get_total_balance(cls, user_id):
        bal = 0
        for coin_addr in cls.__subclasses__():
            bal += coin_addr.objects.get(user=user_id).balance
        return bal

    @classmethod  # Returns each instance of user's wallet (different coins)
    def get_user_moneybag(cls, user_id):
        moneybag = []
        for coin_addr in cls.__subclasses__():
            moneybag.append(coin_addr.objects.get(user=user_id))
        return moneybag

    # 8 decimal places
    @classmethod
    def get_btc_value(cls, user_id):
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

    # get current usd value based on balance
    # So from all the coins subclass we check for the subclass of BTC if it exists
    # if the current BTC balance of user = 0 then return 0
    # else convert the current balance to USD using the coinbin wrapper and return that value
    @classmethod
    def get_usd_value(cls , user_id):
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            if user_object.currency_ticker == 'BTC':
                if user_object.balance == 0:
                    return 0
            else:
                current_usd_value = decimal.Decimal(convert_usd(user_object.currency_ticker, user_object.balance))
        return current_usd_value

        pass


    # *** Below methods needs to be constantly synced with server *** 
    # *** Both the return statements produce the same results ***
    # *** Not tested if it makes a difference due to constant update yet ***
    # *** Not tested example : AddressABC.__transaction_count = something and AddressABC.transaction_count = something ***
    # *** AddressABC.__transaction_count is accessing transaction_count as a private variable ***
    # *** Not sure which value to return ***
    # *** But its mostly wrong I assume ***
    @classmethod
    def fetch_tx_count(cls,user_id):
        # blockchain: keep tx count synced
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            current_tx_count += user_object.transaction_count

        #user_object.transaction_count = current_tx_count    
        user_object.__transaction_count += current_tx_count

        #return current_tx_count
        return user_object.__transaction_count      

    @classmethod
    def fetch_balance(cls,user_id):
        # blockchain: keep balance synced
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            current_balance += user_object.balance

        #user_object.balance = current_balance
        user_object.__balance = current_balance

        #return current_balance
        return user_object.__balance
        

    @classmethod
    def fetch_amt_in(cls,user_id):
        # blockchain
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            current_ammount_in += user_object.amount_in

        #user_object.amount_in = current_ammount_in
        user_object.__amount_in = current_ammount_in

        #return current_ammount_in
        return user_object.__amount_in

    @classmethod
    def fetch_amt_out(cls,user_id):
        # blockchain
        for coin_addr in cls.__subclasses__():
            user_object = coin_addr.objects.get(user=user_id)
            current_ammount_out += user_object.amount_out

        #user_object.amount_out = current_ammount_out
        user_object.__amount_out = current_ammount_out

        #return current_ammount_out
        return user_object.__amount_out

    class Meta:
        abstract = True


# TODO might need to convert this to a concrete class as we need to refer
# to it in the transactions table

class CurrencyABC(models.Model):
    """
    Description: Abstract base class for Cryptocoin Currency model
    """
    currency_name = models.CharField(max_length=32, editable=False)
    currency_ticker = models.CharField(max_length=16, editable=False)
    currency_min_div_unit = models.DecimalField(
        max_digits=12, decimal_places=12, editable=False)
    currency_symbol = models.CharField(max_length=2, null=True, editable=False)
    
    @classmethod
    def get_list_of_coins(cls,user_id):
        coin_name = list()
        c_name = dict()
        i = 0
        for coin_list in cls.__subclasses__():
            coin_name.append(coin_list.objects.get(user=user_id).currency_name)
            inv = {coin_name[i] : coin_name[i]}
            c_name.update(inv)
            i += 1

        # coin_name displays a list json and c_name displays a dictonary json and also the json can be dumped to a temp file
        # if needed 

        #coin_json = json.dumps(coin_name)
        coin_json = json.dumps(c_name)
        return coin_json

    class Meta:
        abstract = True


class BitcoinAddress(AddressABC, CurrencyABC):
    """
    Description: Bitcoin Address model which stores and generates the pub/sec key pair
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
    Description: Litecoin Address model which stores and generates the pub/sec key pair
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


# Maybe make a transactions app to handle wallet transactions?

"""


class TransactionsABC(models.Model):
    TRANSACTION_TYPES = (
        ('S', 'Send'),
        ('R', 'Receive'),
    )

    STATUSES = (
        ('PEN', 'Pending'),
        ('PRO', 'Processing'),
        ('COM', 'Completed'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES)
    transaction_id = models.CharField(max_length=64)

    # TODO Not there in deposit, but there in withdrawals
    amount = models.DecimalField(max_digits=64, decimal_places=16)

    # TODO Not there in deposit, but there in withdrawals
    fee = models.DecimalField(max_digits=64, decimal_places=16)
    confirmations = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    received_at = models.DateTimeField()

    # TODO Status is not needed
    # status = models.CharField(max_length=3, choices=STATUSES)

    # TODO add from and to address fields; think of a nice way to do this
    # TODO add currency id foreign key, so we can use only one deposit and withdrawal table

    def __str__(self):
        return self.transaction_id

    @classmethod
    def deposit(userid,coin,to_address):
        pass

    @classmethod
    def withdraw(userid,coin,to_address):
        pass


    class Meta:
        abstract = True


class Deposits(TransactionABC): # TODO
    from_address


class Withdrawals(TransactionABC): # TODO
    to_address
"""
