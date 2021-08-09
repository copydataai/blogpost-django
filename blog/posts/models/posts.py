"""Posts models."""

# Django
from django.db import models
from ckeditor.fields import RichTextField

# Utilities
from blog.utils.models import BPostModel

# Models
from blog.users.models import Profile

class Post(BPostModel):
    """Post model."""
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='posts/photos')
    content = RichTextField()

    class Meta:
        ordering = ('title')

    def __str__(self):
        """Return Title and username"""
        return f'{self.title} by @{self.user.username}'
