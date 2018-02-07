from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from bit import Key

from wallet.models import Wallet

# Create your models here.


class AddressABC(models.Model):
    """
    Description: Abstract base class for Cryptocoin Address model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    ticker = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    currency_min_divisible_unit = models.DecimalField(
        max_digits=16, decimal_places=16)
    currency_symbol = models.CharField(max_length=16)
    sec_key = models.CharField(
        max_length=128, unique=True, editable=False)
    pub_key = models.CharField(
        max_length=64, unique=True, editable=False)

    class Meta:
        abstract = True


class BitcoinAddress(AddressABC):
    """
    Description: Bitcoin Address model which stores and generates the pub/sec key pair
    """
    batwa = GenericRelation(Wallet)

    def __init__(self, *args, **kwargs):
        super(BitcoinAddress, self).__init__(*args, **kwargs)
        if self.sec_key == '' and self.pub_key == '':
            # if nothing is there, create, convert and set
            self.sec_key = str(Key().to_hex())
            self.pub_key = str(Key().address)
            self.currency_min_divisible_unit = 0.00000001

    def Key(self):
        return Key.from_hex(self.sec_key)

    def __str__(self):
        return self.pub_key

    class Meta:
        verbose_name = 'Bitcoin Address'
        verbose_name_plural = 'Bitcoin Addresses'
