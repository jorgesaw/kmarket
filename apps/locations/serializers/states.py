"""State serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.locations. models import State

class StateModelSerializer(serializers.ModelSerializer):
    """State model serializer."""

    class Meta:
        model = State
        fields = (
            'name', 'slug_name'
        )


