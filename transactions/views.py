from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import TransactionsABC
from moneybag.models import AddressABC
from transactions.wrappers import t_wrapper

# send_transaction(uid, private_key, amount, withdrawal_address, ticker):

@login_required
def process_withdrawal(request):

	# This gets the current logged in user
	current_user = request.user
	current_user_id = current_user.id

	# list of all subclasses
	address_subc = AddressABC.__subclasses__()

	for i in range(len(address_subc)):
		if(address_subc[i] == AddressABC.__subclasses__()[i]):
			#address lite = current coin class
			if(request.POST['something'] == address_subc[i]):
				coin_address = address_subc[i]
				return coin_address
			else:
				continue
		else:
			break

	# get the objects for the coin
	key_address_obj = coin_address.objects.get(current_user_id)

	# get the sec_key for that coin
	key_address = key_address_obj.sec_key

	# get the coin ticker 
	key_symbol = key_address_obj.currency_ticker

	# needs a functional website to test
	# if request.method == 'POST':
	# 	if(request.POST['something'] == 'deposit'):
	# 		amount = request.post['deposit']

	amount = 10

	withdraw_hash = t_wrapper.send_transaction(current_user_id, key_address, amount, key_address, key_symbol )

	return withdraw_hash


def home(request):

	#return render_to_response("transactions/home.html")
	return render(request, 'home.html' , {})