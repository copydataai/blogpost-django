"""Profile model."""

# Django
from django.db import models

# Utilities
from blog.utils.models import BPostModel

class Profile(BPostModel):
    """Profile model."""

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

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
