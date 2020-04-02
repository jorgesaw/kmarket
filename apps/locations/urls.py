"""Locations URLs."""
 
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import states as states_views
from .views import cities as cities_views


router = DefaultRouter()
router.register('states', states_views.StateViewSet, basename='state')
router.register('cities', cities_views.CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)), 
]
