from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from koinrex.users.models import User


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


class Wallet(models.Model):
    """
    Description: Wallet model that stores information with regards to a particular connected address
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    usd_balance = models.DecimalField(max_digits=64, decimal_places=8)
    balance = models.DecimalField(max_digits=64, decimal_places=16)
    amount_in = models.DecimalField(max_digits=64, decimal_places=16)
    amount_out = models.DecimalField(max_digits=64, decimal_places=16)

    # Using ContentType to create generic relations between wallet and address
    # models
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "{}'s Wallet".format(self.user.name)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'


class Transaction(models.Model):
    """
    Description: Transaction model that stores data regarding a deposit or a withdrawal
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
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
