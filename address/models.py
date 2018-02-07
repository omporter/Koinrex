from django.db import models
from wallet.models import *

from bit import Key

# Create your models here.


class BitcoinAddress(models.Model):
    """
    Description: Model Description
    """
    s_key = models.CharField(
        max_length=128, unique=True, editable=False)
    p_key = models.CharField(
        max_length=64, unique=True, editable=False)

    currency = models.OneToOneField(Currency, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(BitcoinAddress, self).__init__(*args, **kwargs)
        if self.s_key == '' and self.p_key == '':
            # if nothing is there, create, convert and set
            self.s_key = str(Key().to_hex())
            self.p_key = str(Key().address)

    def Key(self):
        return Key.from_hex(self.p_key)

    def __str__(self):
        return self.p_key

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
