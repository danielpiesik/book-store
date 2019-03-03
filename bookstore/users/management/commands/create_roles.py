from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

# GROUPS = {
#     'admin': [],
#     'buyer': [],
# }


GROUPS = ['admin', 'buyer']
# MODELS = ['video', 'article', 'license', 'list', 'page', 'client']


class Command(BaseCommand):
    def handle(self, *args, **options):
        for group_name in GROUPS:
            group, created = Group.objects.get_or_create(name=group_name)
