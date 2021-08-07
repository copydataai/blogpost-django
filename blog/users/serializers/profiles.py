"""Profile serializer."""

from rest_framework import serializers

from blog.users.models import Profile

class ProfileModelSerializer(serializers.Serializer):
    """Profile model serializer."""

    class Meta:
        """Meta class."""
        model = Profile
        fields = (
            'picture',
            'biography'
        )
