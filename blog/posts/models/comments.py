"""Commets models."""

# Django
from django.db import models

# Utilities
from blog.utils.models import BPostModel

# Models
from blog.users.models import User, Profile
from .posts import Post

class Comment(BPostModel):
    """Comments model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='posts/comments/photos', blank=True, null=True)

    class Meta:
        ordering = 'created'

    def __str__(self):
        """Return username."""
        return f'{self.user.username} commented this post.'
