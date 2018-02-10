from bit import Key


class Keygen():

    def __init__(self):
        self.key = Key()
        self.sec = ''
        self.pub = ''

    def prv_key(self):
        try:
            self.sec = self.key.to_wif()
            return self.sec
        except:
            print('Error in generating private key, try again.')

    def pub_key(self):
        try:
            self.sec = self.key.address
            return self.sec
        except:
            print('Error in generating public key, try again.')


def keygen():
    k = Key()
    pub = k.address
    sec = k.to_wif()
    return pub, sec
