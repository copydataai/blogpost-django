"""Commets models."""

# Django
from django.db import models

# Utilities
from blog.utils.models import BPostModel

# Models
from blog.users.models import User, Profile

class CommentModel(BPostModel):
    """Comments model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    content = models.CharFIeld(max_length=500)
    photo = models.ImageField(upload_to='posts/comments/photos', blank=True, null=True)

    class Meta:
        ordering = 'created'

    def __str__(self):
        """Return username."""
        return f'{self.user.username} commented this post.'
