from django.shortcuts import render

# Create your views here.

from .models import AddressABC, CurrencyABC, BitcoinAddress, LitecoinAddress
from koinrex.users.models import User
import json
import requests
from itertools import zip_longest
import ast

def home(request):
    #Get current user id
    current_user = request.user
    current_user_id = current_user.id
    
    results = AddressABC.get_all_balance(current_user_id).content.decode()
    result = ast.literal_eval(results)
     
    context = {'coins': result}
    return render(request, 'moneybag/wallet_home.html', context)

def withdrawals(request):
    current_user = request.user
    current_user_id = current_user.id

    get_coin_details = AddressABC.get_all_balance(current_user_id).content.decode()
    result = ast.literal_eval(get_coin_details)
    # print("------------------------", result)
    coin = request.GET['coin']
    for key,val in result.items():
        if (val['user_coin'] == coin):
            ticker = val['currency_ticker']
            balance = val['user_balance']
    context = {'coin_name' : coin,
               'coin_ticker' : ticker,
               'balance' : balance,
        }
    return render(request, 'moneybag/wallet_withdrawal.html', context)
