"""States views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Filters
from rest_framework.filters import OrderingFilter, SearchFilter

# Models
from apps.locations.models import (
    City, State
)

# Serializers
from apps.locations.serializers import (
    CityModelSerializer, 
    CityWithStateModelSerializer, 
    UpdateCityModelSerializer
)


class CityViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """City view set."""

    serializer_class = CityModelSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug_name'

    # Filters
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', 'slug_name')
    ordering_fields = ('name', 'created')
    ordering = ('name',)


    def get_queryset(self):
        """Restrict list to active-only."""

        queryset = City.objects.all()
        if self.action == 'list':
            queryset.filter(active=True)
        return queryset

    def get_serializer_class(self):
        """Return serializer based on action."""

        if self.action in ['create', 'retrieve']:
            return CityWithStateModelSerializer
        elif self.action == 'update':
            return UpdateCityModelSerializer
        return CityModelSerializer

    def create(self, request, *args, **kwargs):
        """Handle."""

        state_slug_name = request.data.pop('slug_name')
        serializer = self.get_serializer_class()(
            data=request.data, 
            context={'state_slug_name': state_slug_name}
        )
        serializer.is_valid(raise_exception=True)
        city = serializer.save()

        data = self.get_serializer(city).data
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        state_slug_name = request.data.pop('state_slug_name')
        serializer = self.get_serializer_class()( 
            instance, 
            data=request.data, 
            context={'state_slug_name': state_slug_name}, 
        )
        
        serializer.is_valid(raise_exception=True)
        #import ipdb; ipdb.set_trace()
        city = serializer.save()

        data = self.get_serializer(city).data
        return Response(data, status=status.HTTP_200_OK)