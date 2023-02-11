from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from setup.models import TimeStampMixin


class Profile(TimeStampMixin):
    about = models.TextField()
    joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Joined'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.about)

    class Meta:
        managed = True
        db_table = u'profile'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profile')
