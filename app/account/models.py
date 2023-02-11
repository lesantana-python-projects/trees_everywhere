from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from setup.models import TimeStampMixin


class Account(TimeStampMixin):
    name = models.CharField(unique=True, max_length=255, blank=False)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = u'account'
        verbose_name = _('Account')
        verbose_name_plural = _('Account')
