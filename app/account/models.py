from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from setup.models import TimeStampMixin


class CustomUser(AbstractUser):
    about = models.TextField(blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Joined'))
    is_staff = models.BooleanField(
        ('staff status', ),
        default=True,
        help_text='Designates whether the user can log into this admin site.',
    )

    class Meta:
        managed = True
        db_table = u'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Account(TimeStampMixin):
    name = models.CharField(unique=True, max_length=255, blank=False)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = u'account'
        verbose_name = _('Account')
        verbose_name_plural = _('Account')
