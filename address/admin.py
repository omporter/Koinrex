from django.contrib import admin

from .models import BitcoinAddress, LitecoinAddress

# Register your models here.

admin.site.register(BitcoinAddress)
admin.site.register(LitecoinAddress)
