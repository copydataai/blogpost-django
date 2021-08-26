"""Comments serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from blog.posts.models import Comment


class CommentModelSerializer(serializers.Serializer):
    """Comment model serialzer."""

    class Meta:
        """Meta class."""

        model = Comment
        field = ('comment', 'photo')
