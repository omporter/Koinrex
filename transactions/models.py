import uuid

from django.db import models

from moneybag.models import AddressABC
from koinrex.users.models import User

# Create your models here.


class TransactionsABC(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    koinrex_tx_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    confirmations = models.IntegerField()
    user_address = models.CharField(
        max_length=64)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tx_hash = models.CharField(max_length=128)

    # TODO Status is not needed
    # status = models.CharField(max_length=3, choices=STATUSES)

    # TODO add from and to address fields; think of a nice way to do this
    # TODO add currency id foreign key, so we can use only one deposit and
    # withdrawal table

    def __str__(self):
        return self.transaction_id

    @classmethod
    def deposit(userid, coin, to_address):
        pass

    @classmethod
    def withdraw(userid, coin, to_address):
        pass

    class Meta:
        abstract = True


class Deposits(TransactionsABC):
    from_address = models.CharField(
        max_length=64, unique=True, editable=False)

    class Meta:
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposits'


class Withdrawals(TransactionsABC):
    to_address = models.CharField(
        max_length=64, unique=True, editable=False)
    amount = models.DecimalField(max_digits=64, decimal_places=16)
    #fee = models.DecimalField(max_digits=64, decimal_places=16)

    class Meta:
        verbose_name = 'Withdrawal'
        verbose_name_plural = 'Withdrawals'
