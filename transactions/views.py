from django.shortcuts import render,render_to_response , redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import TransactionsABC
from moneybag.models import AddressABC,CurrencyABC, BitcoinAddress, LitecoinAddress
from koinrex.users.models import User
from transactions.wrappers import t_wrapper
import json
from itertools import zip_longest
import ast
import time
from django.views.decorators.csrf import csrf_exempt 
# send_transaction(uid, private_key, amount, withdrawal_address, ticker):
from .forms import WithdrawalForms


'''
To note request.POST['withdraw'] comes from submit button which is currency ticker from html 
and currency ticker should always be there for this to work

changes made to models and froms 

'''
# for withdraw
@login_required
def home(request):


	current_user = request.user
	current_user_id = current_user.id

	results = AddressABC.get_all_balance(current_user_id).content.decode()
	result = ast.literal_eval(results)
	form = WithdrawalForms()
	obj = AddressABC.__subclasses__()
	context = {'coins': result,'form' : form}

	if request.method == 'POST':
		form = WithdrawalForms(request.POST)
		#print(request.POST)
		coint_tick = request.POST['withdraw']
		#print(a)
		if form.is_valid():
			withdraw_confirm = WithdrawalForms(request.POST)
			to_withdraw_address = withdraw_confirm['to_address'].value()
			withdraw_amount = int(withdraw_confirm['amount'].value())

			for i in range(len(obj)):
				if(obj[i] == coin_tick):
					secret = obj[i].objects.get(id=current_user.id).sec_key
					#withdraw_hash = t_wrapper.send_transaction( secret , withdraw_amount,  to_withdraw_address , coin_tick)
					withdraw_hash = 'adebc98565129883f58cac7ee2740a8ff64a02d1fe83120a1f0c63fb2bfe8e65'
			
					TransactionsABC = form.save(commit = False)
					TransactionsABC.user_address = to_withdraw_address
					TransactionsABC.user = current_user
					TransactionsABC.tx_hash = withdraw_hash
					#TransactionsABC.confirmations = 1
					TransactionsABC.save()
				
	return render(request, 'transactions/home.html' , context)

