from bit import Key, PrivateKeyTestnet
import blockcypher

from blockcypher import simple_spend, get_token_info

from moneybag.models import AddressABC


''' fetch balances from blockchain'''
def litecoin_balance(litecoin_public_key):
    litecoin_public_key = str(litecoin_public_key)
    sat_balance = blockcypher.get_total_balance(litecoin_public_key, 'ltc')
    ltc_balance = blockcypher.from_satoshis(sat_balance, 'btc')
    return ltc_balance

def ethereum_balance(ethereum_public_key):
    # ethereum_public_key = str(ethereum_public_key)
    # wei_balance = blockcypher.get_total_balance(ethereum_public_key, 'eth')
    # return wei_balance
    pass
    ''' BLOCKCYPHER NOW HAS AN ETHEREUM LIBRARY, CHECK IT OUT'''

def bitcoin_balance(bitcoin_public_key):
    bitcoin_public_key = str(bitcoin_public_key)
    sat_balance = blockcypher.get_total_balance(bitcoin_public_key)
    btc_balance = blockcypher.from_satoshis(sat_balance, 'btc')
    return btc_balance

def dash_balance(dash_public_key):
    dash_public_key = str(dash_public_key)
    sat_balance = blockcypher.get_total_balance(dash_public_key, 'dash')
    dash_balance = blockcypher.from_satoshis(sat_balance, 'btc')
    return dash_balance


''' fetch number of transactions on that address to date'''
def litecoin_address_current_transactions(litecoin_public_key):
    litecoin_public_key = str(litecoin_public_key)
    transactions = blockcypher.get_total_num_transactions(litecoin_public_key, 'ltc')
    return transactions


def ethereum_address_current_transactions(ethereum_public_key):
    # ethereum_public_key = str(ethereum_public_key)
    # transactions = blockcypher.get_total_num_transactions(ethereum_public_key)
    # return transactions
    ''' BLOCKCYPHER NOW HAS AN ETHEREUM LIBRARY, CHECK IT OUT'''
    pass 
    
def bitcoin_address_current_transactions(bitcoin_public_key):
    bitcoin_public_key = str(bitcoin_public_key)
    transactions = blockcypher.get_total_num_transactions(bitcoin_public_key)
    return transactions

def dash_address_current_transactions(dash_public_key):
    dash_public_key = str(dash_public_key)
    transactions = blockcypher.get_total_num_transactions(dash_public_key, 'dash')
    return transactions



# api_key = '8763ec6f2f164f508feff8205b1e6b33'
# priv_key = '1de5e4cdb0391d3a95dbb892b9c317202c0a263d8621daba0cf682ca5d11ed36'
# to_address = 'LMU9ZqvhVDZd2mGCnYMvjRwLnKNPgiPoCG'


# transaction_hash = simple_spend(from_privkey=priv_key, to_address=to_address, to_satoshis=50000, change_address=None, privkey_is_compressed=False, min_confirmations=0, api_key=api_key, coin_symbol='ltc')

# print(transaction_hash)



''' send a transaction from the private key '''

def send_transaction(uid, private_key, amount, withdrawal_address, ticker):
    if amount == None:
        amount = 0
    api_key = '8763ec6f2f164f508feff8205b1e6b33' # TODO use a koinrex API 
    amount_in_sats = (float(amount) * 100000000)
    ticker = str(ticker.lower())
    # mining_fee = (amount * 0.005) # take 0.5% for now for the sake of argument until we work out how to calculate mining fee
    transaction_hash = simple_spend(from_privkey=str(private_key), to_address=str(withdrawal_address), to_satoshis=amount_in_sats, change_address=None, privkey_is_compressed=False, min_confirmations=0, api_key=api_key, coin_symbol=ticker)
    return transaction_hash


# simple_spend(from_privkey='97838249d77bfa65f97be02b63fd1b7bb6a58474c7c22784a0da63993d1c2f90', to_address='C1rGdt7QEPGiwPMFhNKNhHmyoWpa5X92pn', to_satoshis=1000000, coin_symbol='bcy')






# btc = '1CZ3CbtA3Rs3PcnK2PE9kSVDf85HWM9EcH'
# dash = 'XhLHR1ryrbJV71NJqQKEqsp3DTHbaVfmps'
# ltc = 'LVuEP2jgj1YyFnneZFmJFyyB1Tj28yj41t'
# eth = '0xc3CaE45cD278F235fF5ff2D8f0e7c0971955c600'


# print(generate_new_bitcoin_address())
# print(dash_balance(dash))
# print(litecoin_balance(ltc))
# print(bitcoin_balance(btc))
# print(bitcoin_address_current_transactions(btc))
# print(litecoin_address_current_transactions(ltc))
# print(dash_address_current_transactions(dash))
