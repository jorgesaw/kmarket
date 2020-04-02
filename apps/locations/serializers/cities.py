"""City serializers."""

# Django REST Framework
from rest_framework import serializers

# Serializers
from apps.locations.serializers import StateModelSerializer 

# Models
from apps.locations. models import City, State

class CityModelSerializer(serializers.ModelSerializer):
    """City model serializer."""

    class Meta:
        model = City
        fields = (
            'name',
            'slug_name', 
            'zip_city', 
            'ddn'
        )

class CityWithStateModelSerializer(serializers.ModelSerializer):
    """City with statemodel serializer."""

    state = StateModelSerializer(read_only=True)

    class Meta(CityModelSerializer.Meta):
        fields = (
            'name',
            'slug_name', 
            'zip_city', 
            'ddn', 
            'state' 
        )

    def validate(self, data):
        """Verify state exists."""

        state_slug_name = self.context['state_slug_name']
        try:
            state = State.objects.get(
                slug_name=state_slug_name
            )
        except State.DoesNotExist:
            raise serializers.ValidationError('State does not exists.')
        self.context['state'] = state 
        return data

    def create(self, data):
        """Create new city."""
        import ipdb; ipdb.set_trace()
        state = self.context['state']
        city = City.objects.create(**data, state=state)
        return city

class UpdateCityModelSerializer(serializers.ModelSerializer):
    """City with statemodel serializer."""

    state = StateModelSerializer(read_only=True)

    class Meta(CityModelSerializer.Meta):
        fields = (
            'name',
            'slug_name', 
            'zip_city', 
            'ddn', 
            'state' 
        )

    def validate(self, data):
        """Verify state exists."""

        state_slug_name = self.context['state_slug_name']
        try:
            state = State.objects.get(
                slug_name=state_slug_name
            )
        except State.DoesNotExist:
            raise serializers.ValidationError('State does not exists.')
        self.context['state'] = state 
        return data

    def update(self, instance, data):
        """Update data for the city."""

        #import ipdb; ipdb.set_trace()

        state = self.context['state']
        #city = instance.save(**data, state=state)
        instance.name = data.get('name', instance.name)
        instance.state = state
        instance.save()
        return instance