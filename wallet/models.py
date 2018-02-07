from django.db import models
from koinrex.users.models import User

from address.models import BitcoinAddress

# Create your models here.


TRANSACTION_TYPES = (
    ('S', 'Send'),
    ('R', 'Receive'),
)

STATUSES = (
    ('PEN', 'Pending'),
    ('PRO', 'Processing'),
    ('COM', 'Completed'),
)


class Currency(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=64)
    ticker = models.CharField(max_length=16)
    min_divisible_unit = models.DecimalField(max_digits=16, decimal_places=16)
    symbol = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class Wallet(models.Model):
    """
    Description: Model Description
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=64, decimal_places=16)
    usd_balance = models.DecimalField(max_digits=64, decimal_places=8)
    amount_in = models.DecimalField(max_digits=64, decimal_places=16)
    amount_out = models.DecimalField(max_digits=64, decimal_places=16)
    address = models.OneToOneField(
        BitcoinAddress, on_delete=models.PROTECT)

    def __str__(self):
        return "{}'s Wallet".format(self.user.name)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'


class Transaction(models.Model):
    """
    Description: Model Description
    """
    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPES)
    transaction_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=64, decimal_places=16)
    fee = models.DecimalField(max_digits=64, decimal_places=16)
    confirmations = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField()
    status = models.CharField(max_length=3, choices=STATUSES)

    # TODO add from and to address fields; think of a nice way to do this

    def __str__(self):
        return self.transaction_id

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class Portfolio(models.Model):
    """
    Description: Model Description
    """
    pass

    class Meta:
        pass
