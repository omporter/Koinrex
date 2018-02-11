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
# send_transaction(uid, private_key, amount, withdrawal_address, ticker):

# @login_required
# def process_withdrawal(request):

# 	# This gets the current logged in user
# 	current_user = request.user
# 	current_user_id = current_user.id

# 	# list of all subclasses
# 	address_subc = AddressABC.__subclasses__()

# 	# iterate through the list of all subclasses that exist
# 	for i in range(len(address_subc)):
# 		# if the request['something'] == bitcoin then it goes into the if statement
# 		if(request.POST['something'] == address_subc[i].objects.get(current_user_id).currency_name):
# 			# then assigns the current subclass to coin_address which will be used to get keys and stuff
# 			coin_address = address_subc[i]

# 			# get the objects for the coin
# 			key_address_obj = coin_address.objects.get(current_user_id)

# 			# get the sec_key for that coin
# 			key_address = key_address_obj.sec_key

# 			# get the coin ticker 
# 			key_symbol = key_address_obj.currency_ticker

# 			# needs a functional website to test
# 			# if request.method == 'POST':
# 			# 	if(request.POST['something'] == 'deposit'):
# 			# 		amount = request.post['deposit']

# 	amount = 10

# 	withdraw_hash = t_wrapper.send_transaction(current_user_id, key_address, amount, key_address, key_symbol )

# 	return withdraw_hash

@login_required
def home(request):
	# current_user = request.user
	# current_user_id = current_user.id

	# results = AddressABC.get_all_balance(current_user_id).content.decode()
	# result = ast.literal_eval(results)

	# context = {'coins': result}

	# print(result)

	# if request.method == 'POST':
	# 	print(request.POST)
	# 	a = request.POST['withdraw']
	# 	print(a)
	# 	# list of all subclasses

	amount = 1000
	withdraw_hash = t_wrapper.send_transaction( '1de5e4cdb0391d3a95dbb892b9c317202c0a263d8621daba0cf682ca5d11ed36' , amount,  'LVuEP2jgj1YyFnneZFmJFyyB1Tj28yj41t' , 'ltc')
		# hash_store = TransactionsABC(confirmations=1,user_address=key_address, user = current_user, tx_hash = withdraw_hash)
		# hash_store.save()
	print("withdraw hash ",withdraw_hash)
	# return withdraw_hash
	#return HttpResponseRedirect('')
	# return render(request, 'transactions/home.html' , context)
# 


# from blockcypher import simple_spend
# simple_spend(from_privkey='1de5e4cdb0391d3a95dbb892b9c317202c0a263d8621daba0cf682ca5d11ed36', to_address='LVuEP2jgj1YyFnneZFmJFyyB1Tj28yj41t', to_satoshis=10000, coin_symbol='ltc')
