from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations

from setup.config import get_config

config_app = get_config()


def add_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    User.objects.create(
        email='admin@youshop.com',
        password=make_password(config_app.ADMIN_PASS),
        username='admin',
        is_superuser=True,
        is_staff=True
    )


def remove_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    User.objects.get(email='admin@youshop.com').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0003_profile_joined'),
    ]

    operations = [
        migrations.RunPython(add_user, remove_user),
    ]
