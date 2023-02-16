from django.test import TestCase

from app.account.models import Account, CustomUser
from app.tree_everywhere.models import PlantedTree, Tree


class TestAccount(TestCase):

    def setUp(self):
        self.user_1 = CustomUser.objects.create(username='test_1', pk=3)
        self.user_2 = CustomUser.objects.create(username='test_2', pk=4)
        self.user_3 = CustomUser.objects.create(username='test_3', pk=5)

        self.account_1 = Account(name='Account_Test_1', active=True, pk=2)
        self.account_1.save()
        self.account_1.users.add(self.user_1)

        self.account_2 = Account(name='Account_Test_2', active=True, pk=3)
        self.account_2.save()
        self.account_2.users.add(self.user_2)
        self.account_2.users.add(self.user_3)

        PlantedTree.objects.create(
            age=10,
            tree=Tree.objects.order_by('?').first(),
            user=CustomUser.objects.get(pk=3),
            account=Account.objects.get(pk=2),
            latitude=10.555,
            longitude=10.555
        )

        PlantedTree.objects.create(
            age=10,
            tree=Tree.objects.order_by('?').first(),
            user=CustomUser.objects.get(pk=4),
            account=Account.objects.get(pk=3),
            latitude=10.555,
            longitude=10.555
        )

        PlantedTree.objects.create(
            age=10,
            tree=Tree.objects.order_by('?').first(),
            user=CustomUser.objects.get(pk=5),
            account=Account.objects.get(pk=3),
            latitude=10.555,
            longitude=10.555
        )

    def test_sample(self):
        self.assertTrue(True)
