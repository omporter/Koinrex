from bit import Key
# from IPython import embed


class Keygen(Key):
    sec = ''
    pub = ''

    def generate_key(self):
        self.sec = self.to_wif()
        return self.sec

    def pub_key(self):
        self.pub = self.address
        return self.pub

# key1 = Keygen()
# embed()
