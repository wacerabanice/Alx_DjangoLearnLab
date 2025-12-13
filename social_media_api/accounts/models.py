from django.db import models
from django.conf import settings  
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    # Use AUTH_USER_MODEL instead of User
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username