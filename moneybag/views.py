from django.shortcuts import render

# Create your views here.

from .models import AddressABC, CurrencyABC, BitcoinAddress, LitecoinAddress
from koinrex.users.models import User
import json
import requests

def home(request):
    #Get current user id
    current_user = request.user
    current_user_id = current_user.id
        
    #Get Bitcoin and Litecoin addresses
    a = AddressABC.get_user_moneybag(current_user_id)
    json_result = json.loads(a.content)

    #Get List of Coins
    b = CurrencyABC.get_list_of_coins()
    list_coins = json.loads(b.content)

    #Get coin ticker
    coin_ticker = "BTC"

    #Get coin name
    coin_name = "Bitcoin"

    #Get total balance
    c = AddressABC.get_all_balance(current_user_id)
    total_balance = json.loads(c.content)
    e = total_balance[json_result['Bitcoin']]
    d = e['user_balance']
    total_balance = d


    # Get BTC btc_value
    btc_value = AddressABC.get_btc_value(current_user_id)

    coins = {'coin_ticker' : coin_ticker, 'coin_name' : coin_name, 
             'total_balance' : total_balance, 'btc_value' :btc_value}
    
    context = { 'sample' : d,'coins' : coins,}
    return render(request, 'moneybag/wallet_home.html', context)
