from django.db import models

# Create your models here.


ASSET_TYPES = (
    ('FOO', 'Footype'),
    ('BAR', 'Bartype'),
)


class Currency(models.Model):
    """
    Description: Model Description
    """
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    min_divisible_unit = models.DecimalField(decimal_places=20)
    symbol = models.CharField(max_length=10)
    asset_type = models.CharField(max_length=3, choices=ASSET_TYPES)

    class Meta:
        pass


class Address(models.Model):
    """
    Description: Model Description
    """
    public_key = models.CharField(max_length=None)

    class Meta:
        pass
