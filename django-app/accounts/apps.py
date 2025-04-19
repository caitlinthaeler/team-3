from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group

def create_default_groups(sender, **kwargs):
    for name in ('Teacher', 'Student'):
        Group.objects.get_or_create(name=name)

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        post_migrate.connect(create_default_groups, sender=self)
