from django import forms
from django.forms import ModelForm
from transactions.models import Withdrawals, Deposits



class WithdrawalForms(forms.ModelForm):

	class Meta:
		model = Withdrawals
		fields = ('to_address','amount')


class Deposits(forms.Form):

	class meta:
		model = Deposits
		fields = ('from_address')

