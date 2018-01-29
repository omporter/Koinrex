from bit import Key

key = Key()


def generate_key():
    return key


def show_pub_key():
    return key.address
