"""Posts serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from blog.posts.models import Post

class PostModelSerializer(serializers.Serializer):
    """Post model serializer."""


    class Meta:
        """Meta class."""

        model = Post
        field = (
            'title',
            'content'
            )
