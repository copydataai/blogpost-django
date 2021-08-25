"""Profile model."""

# Django
from django.db import models

# Models
from .users import User

# Utilities
from blog.utils.models import BPostModel

class Profile(models.Model):
    """Profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
