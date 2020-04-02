"""Profiles serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """Porfile model serializer."""

    class Meta:
        model = Profile
        fields = (
            'picture', 
            'biography'
        )

        read_only_fields = ()
