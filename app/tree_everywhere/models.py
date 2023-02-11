from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.account.models import Account
from setup.models import TimeStampMixin


class Tree(TimeStampMixin):
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)
    scientific_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = u'tree'
        verbose_name = _('Tree')
        verbose_name_plural = _('Trees')


class PlantedTree(TimeStampMixin):
    age = models.IntegerField(blank=False, null=False)
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, default=None, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, default=None, on_delete=models.CASCADE)
    location = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=False)

    def __str__(self):
        return str(self.age)

    class Meta:
        managed = True
        db_table = u'planted_tree'
        verbose_name = _('PlantedTree')
        verbose_name_plural = _('PlantedTree')
