"""States views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Filters
from rest_framework.filters import OrderingFilter, SearchFilter

# Models
from apps.locations.models import City, State

# Serializers
from apps.locations.serializers import StateModelSerializer
from apps.locations.serializers import CityModelSerializer

class StateViewSet(viewsets.ModelViewSet):
    """State view set."""

    serializer_class = StateModelSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug_name'

    # Filters
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', 'slug_name')
    ordering_fields = ('name', 'created')
    ordering = ('name',)

    def get_queryset(self):
        """Restrict list to active-only."""

        queryset = State.objects.all()
        if self.action == 'list':
            queryset.filter(active=True)
        return queryset

    @action(detail=True, methods=['get',])
    def cities(self, request, *args, **kwargs):
        """Will return all cities by state."""

        state = self.get_object()
        cities = City.objects.filter(
            state=state,
            active=True
        )
        data = {
            'state': self.get_serializer(state).data, 
            'cities': CityModelSerializer(cities, many=True).data
        }

        return Response(data)