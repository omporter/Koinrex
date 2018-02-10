import blockcypher


def address_current_transactions(pub_key, ticker):
    key = str(pub_key)
    cur_tx = blockcypher.get_total_num_transactions(key, ticker)
    return cur_tx


def address_current_balance(pub_key, ticker):
    key = str(pub_key)
    cur_bal = blockcypher.get_total_balance(key, ticker)
    bal = blockcypher.from_satoshis(cur_bal, 'btc')
    return bal


def address_received(pub_key, ticker):
    key = str(pub_key)
    overview = blockcypher.get_address_overview(key, ticker)
    received = overview['total_received']
    rec = blockcypher.from_satoshis(received, 'btc')
    return rec


def address_sent(pub_key, ticker):
    key = str(pub_key)
    overview = blockcypher.get_address_overview(key, ticker)
    received = overview['total_sent']
    rec = blockcypher.from_satoshis(received, 'btc')
    return rec
