from django.test import TestCase
from .models import BitcoinAddress, LitecoinAddress
from address.wrappers.litecoin import LTCKey

# Create your tests here.


class BitcoinAddressTestCase(TestCase):

    def test_create_auto(self):
        # Test creation
        ba = BitcoinAddress.objects.create()
        self.assertNotEqual(ba, None)
        self.assertNotEqual(ba.sec_key, '')

        k = ba.key_object()
        pvt_key = str(k.to_hex())
        pub_key = str(k.public_key)

        # Test you don't overwrite it when loading from db
        fresh = BitcoinAddress.objects.get(id=1)
        self.assertEqual(pvt_key, str(fresh.key_object().to_hex()))
        self.assertEqual(pub_key, str(fresh.key_object().public_key))


class LitecoinAddressTestCase(TestCase):

    def test_create_auto(self):
        # Test creation
        la = LitecoinAddress.objects.create()
        self.assertNotEqual(la, None)
        self.assertNotEqual(la.sec_key, '')

        # Generate a new key and test if its not equal to the stored key
        pair = LTCKey()
        pvt_key = str(pair.keyval()['sec_key'])
        pub_key = str(pair.keyval()['pub_key'])

        fresh = LitecoinAddress.objects.get(id=1)
        self.assertNotEqual(pvt_key, str(fresh.sec_key))
        self.assertNotEqual(pub_key, str(fresh.pub_key))

        # Get public and private key from model and test if value exists in
        # database
        pv_key, pu_key = la.key_object()
        self.assertEqual(pu_key, str(fresh.pub_key))
        self.assertEqual(pv_key, str(fresh.sec_key))
