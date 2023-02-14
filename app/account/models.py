from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from setup.models import TimeStampMixin


class Account(TimeStampMixin):
    name = models.CharField(unique=True, max_length=255, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = u'account'
        verbose_name = _('Account')
        verbose_name_plural = _('Account')


class CustomUser(AbstractUser):
    about = models.TextField(blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Joined'))
    is_staff = models.BooleanField(
        ('staff status',),
        default=True,
        help_text='Designates whether the user can log into this admin site.',
    )
    accounts = models.ManyToManyField('Account', through='UserAccount', related_name='users')

    class Meta:
        managed = True
        db_table = u'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class UserAccount(TimeStampMixin):
    user = models.ForeignKey('CustomUser',
                             related_name='user_accounts', on_delete=models.SET_NULL, null=True, blank=False)
    account = models.ForeignKey('Account',
                                related_name='user_accounts', on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        unique_together = ('user', 'account')
        managed = True
        db_table = u'user_account'
