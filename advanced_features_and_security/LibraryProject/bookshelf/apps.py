# bookshelf/apps.py

from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        post_migrate.connect(create_user_groups, sender=self)


def create_user_groups(sender, **kwargs):
    # Create groups
    editors, created = Group.objects.get_or_create(name='Editors')
    viewers, created = Group.objects.get_or_create(name='Viewers')
    admins, created = Group.objects.get_or_create(name='Admins')

    # Assign permissions
    book_permissions = Permission.objects.filter(codename__in=['can_view', 'can_create', 'can_edit', 'can_delete'])
    
    editors.permissions.set(book_permissions.filter(codename__in=['can_create', 'can_edit', 'can_view']))
    viewers.permissions.set(book_permissions.filter(codename__in=['can_view']))
    admins.permissions.set(book_permissions)  # All permissions
