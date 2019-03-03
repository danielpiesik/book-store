from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    role = models.ForeignKey(
        'auth.Group',
        on_delete=models.CASCADE,
        related_name='users',
    )
