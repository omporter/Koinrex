import requests
import json
import decimal

from IPython import embed

base_url = 'https://coinbin.org/'


def convert(coin, to_coin):
    """
    Converts value from one coin to another, does not work with USD
    """
    try:
        url = base_url + coin + '/to/' + to_coin
        res = requests.get(url)
        data = res.content
        obj = json.loads(data)
        return obj['coin']['exchange_rate']
    except:
        return ('Network issue, try again')


def convert_usd(coin, amount):
    """
    Converts value from one coin to USD only
    """
    try:
        url = base_url + coin + '/' + str(amount)
        res = requests.get(url)
        data = res.content
        obj = json.loads(data)
        return obj['coin']['usd']
    except:
        return ('Network issue, try again')

def get_btc_value(balance,ticker):
    rate = convert(ticker, 'BTC')
    btc_val = balance * decimal.Decimal(rate)
    return btc_val

# print(type(convert('btc', 'ltc')))
