"""Posts models."""

# Django
from django.db import models
from ckeditor.fields import RichTextField

# Utilities
from blog.utils.models import BPostModel


class Post(BPostModel):
    """Post model."""
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='posts/photos', blank=True, null=True)
    content = RichTextField()

    class Meta:
        ordering = ('created', 'modified')

    def __str__(self):
        """Return Title and username"""
        return f'{self.title} by @{self.user.username}'
