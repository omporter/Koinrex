from django.contrib import admin

from .models import BitcoinAddress, LitecoinAddress

# Register your models here.


class AddressAdminABC(admin.ModelAdmin):
    list_display = ('id', 'pub_key', 'created_at',
                    'currency_name', 'user', 'balance', 'usd_balance',)
    list_display_links = ('pub_key', 'user', 'currency_name',)
    list_filter = ('user', 'created_at', 'balance',)
    search_fields = ('user', 'created_at')
    list_per_page = 50

    class Meta:
        abstract = True


class BitcoinAddressAdmin(AddressAdminABC):
    pass


class LitecoinAddressAdmin(AddressAdminABC):
    pass


admin.site.register(BitcoinAddress, BitcoinAddressAdmin)
admin.site.register(LitecoinAddress, LitecoinAddressAdmin)
