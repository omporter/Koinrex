from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import requests
import json
import ast
from itertools import zip_longest

from koinrex.users.models import User
from moneybag.models import AddressABC, CurrencyABC, BitcoinAddress, LitecoinAddress
from moneybag.forms import WithdrawalForms
from transactions.models import TransactionsABC
from transactions.wrappers import t_wrapper


# Create your views here.


def home(request):
    # Get current user id
    current_user = request.user
    current_user_id = current_user.id
    # Get all the values needed for the table
    results = AddressABC.get_all_balance(current_user_id).content.decode()
    result = ast.literal_eval(results)

    total_btc_value = AddressABC.get_total_btc_value(current_user_id)
    total_btc_value = round(total_btc_value, 8)

    usd_value = AddressABC.get_usd_value(current_user_id)
    usd_value = round(usd_value, 2)

    context = {'coins': result,
               'usd_value': usd_value,
               'total_btc': total_btc_value}
    return render(request, 'moneybag/wallet_home.html', context)


@login_required
def withdrawals(request):

    current_user = request.user
    current_user_id = current_user.id
    forms = WithdrawalForms()
    get_coin_details = AddressABC.get_all_balance(
        current_user_id).content.decode()

    result = ast.literal_eval(get_coin_details)
    obj = AddressABC.__subclasses__()
    # print("------------------------", result)

    coin = request.GET['coin']

    if request.method == 'POST':
        form = WithdrawalForms(request.POST)
        # print(request.POST)
        coin_tick = request.POST['withdraw']
        print(coin_tick)
        if form.is_valid():
            withdraw_confirm = WithdrawalForms(request.POST)
            to_withdraw_address = withdraw_confirm['to_address'].value()
            withdraw_amount = int(withdraw_confirm['amount'].value())
            print(to_withdraw_address)

            for i in range(len(obj)):
                if(obj[i].objects.get(id=current_user_id).currency_ticker == coin_tick):
                    secret = obj[i].objects.get(id=current_user.id).sec_key
                    withdraw_hash = t_wrapper.send_transaction(
                        secret, withdraw_amount,  to_withdraw_address, coin_tick)
                    #withdraw_hash = 'adebc98565129883f58cac7ee2740a8ff64a02d1fe83120a1f0c63fb2bfe8e65'

                    TransactionsABC = form.save(commit=False)
                    TransactionsABC.user_address = to_withdraw_address
                    TransactionsABC.user = current_user
                    TransactionsABC.tx_hash = withdraw_hash
                    #TransactionsABC.confirmations = 1
                    TransactionsABC.save()
                    return redirect('withdrawals_success')

    for key, val in result.items():
        if (val['user_coin'] == coin):
            ticker = val['currency_ticker']
            balance = val['user_balance']

    context = {'coin_name': coin,
               'coin_ticker': ticker,
               'balance': balance,
               'form': forms,
               }

    return render(request, 'moneybag/wallet_withdrawal.html', context)


def deposits(request):
    current_user = request.user
    current_user_id = current_user.id

    get_coin_details = AddressABC.get_all_balance(
        current_user_id).content.decode()
    result = ast.literal_eval(get_coin_details)
    coin = request.GET['coin']
    for key, val in result.items():
        if (val['user_coin'] == coin):
            ticker = val['currency_ticker']
            balance = val['user_balance']
            address = key

    context = {'coin_name': coin,
               'coin_ticker': ticker,
               'balance': balance,
               'address': address
               }

    return render(request, 'moneybag/wallet_deposit.html', context)


def withdrawals_success(request):
    return render(request, 'moneybag/wallet_withdrawals_success.html')
