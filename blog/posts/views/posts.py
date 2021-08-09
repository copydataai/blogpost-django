"""Posts views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from blog.posts.serializers.posts import PostModelSerializer


# Models
from blog.posts.models import Post

class PostViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """User view set."""

    serializer_class = PostModelSerializer
