from unittest import TestCase

from app.account.models import Account


class TestAccount(TestCase):
    def setUp(self):
        Account.objects.create(name="Account_1")

    def test_xpto(self):
        self.assertTrue(True)
