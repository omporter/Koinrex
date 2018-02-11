from django.db import models

# Create your models here.

# TODO 3 = Maybe make a transactions app to handle wallet transactions?


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
    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPES)
    transaction_id = models.CharField(max_length=64)

    # TODO Not there in deposit, but there in withdrawals
    amount = models.DecimalField(max_digits=64, decimal_places=16)

    # TODO Not there in deposit, but there in withdrawals
    fee = models.DecimalField(max_digits=64, decimal_places=16)
    confirmations = models.IntegerField()
    #wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    received_at = models.DateTimeField()

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


# class Deposits(TransactionABC):  # TODO
#     from_address
    

# class Withdrawals(TransactionABC):  # TODO
#     to_address
#     