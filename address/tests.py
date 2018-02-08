from django.test import TestCase
from .models import BitcoinAddress, LitecoinAddress

# Create your tests here.

# TODO 1 - Refactor Litecoin Test Case


class BitcoinAddressTestCase(TestCase):

    def test_create_auto(self):
        # test creation
        ba = BitcoinAddress.objects.create()
        self.assertNotEqual(ba, None)
        self.assertNotEqual(ba.sec_key, '')

        k = ba.key_object()
        pvt_key = str(k.to_hex())
        pub_key = str(k.public_key)

        # test you don't overwrite it when loading from db
        fresh = BitcoinAddress.objects.get(id=1)
        self.assertEqual(pvt_key, str(fresh.key_object().to_hex()))
        self.assertEqual(pub_key, str(fresh.key_object().public_key))


class LitecoinAddressTestCase(TestCase):

    def test_create_auto(self):
        # test creation
        la = LitecoinAddress.objects.create()
        self.assertNotEqual(la, None)
        self.assertNotEqual(la.sec_key, '')

        # TODO 1

        # k = ba.key_object()
        # pvt_key = str(k.to_hex())
        # pub_key = str(k.public_key)

        # test you don't overwrite it when loading from db
        # fresh = LitecoinAddress.objects.get(id=1)
        # self.assertEqual(pvt_key, str(fresh.key_object().to_hex()))
        # self.assertEqual(pub_key, str(fresh.key_object().public_key))
