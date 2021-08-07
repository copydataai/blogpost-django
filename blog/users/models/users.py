"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#Utilities
from blog.utils.models import BPostModel

class User(BPostModel, AbstractUser):
    """User model."""

    email = models.EmailField(
        'email address',
        unique=True,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
    )

    is_verified = models.BooleanField(
        'verified',
        default=False
    )

    def __str__(self):
        """Return username"""
        return str(self.username)
