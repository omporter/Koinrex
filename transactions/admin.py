from django.contrib import admin

from transactions.models import Deposits, Withdrawals

# Register your models here.


admin.site.register(Deposits)
admin.site.register(Withdrawals)
