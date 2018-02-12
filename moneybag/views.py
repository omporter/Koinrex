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
    #Get all the values needed for the table
    results = AddressABC.get_all_balance(current_user_id).content.decode()
    result = ast.literal_eval(results)

    total_btc_value = AddressABC.get_total_btc_value(current_user_id)
    total_btc_value = round(total_btc_value, 8)
        
    usd_value = AddressABC.get_usd_value(current_user_id)
    usd_value = round(usd_value, 2)
         
    context = { 'coins': result,
                'usd_value' : usd_value,
                'total_btc' : total_btc_value}
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

def deposits(request):
    current_user = request.user
    current_user_id = current_user.id

    get_coin_details = AddressABC.get_all_balance(current_user_id).content.decode()
    result = ast.literal_eval(get_coin_details)
    coin = request.GET['coin']
    for key,val in result.items():
        if (val['user_coin'] == coin):
            ticker = val['currency_ticker']
            balance = val['user_balance']
            address = key

    context = {'coin_name' : coin,
               'coin_ticker' : ticker,
               'balance' : balance,
               'address' : address
                       }


    return render(request, 'moneybag/wallet_deposit.html', context)

