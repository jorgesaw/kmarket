"""City tests."""

# Django
from django.test import TestCase

# Models
from apps.locations.models import City, State

# Utilities
from django.utils.text import slugify


class CityManagerTestCase(TestCase):
    """City manager statetest case."""

    def setUp(self):
        """Test case setup."""
    
        self.name_city = 'Villa Constitución'
        state = State.objects.create(name='STATE TEST')
        self.city = City.objects.create(name=self.name_city, state=state)
        

    def test_slug_name_create(self):
        """if slug_name has created at save."""

        self.assertIsNone(self.city.slug_name)

    def test_slug_name_by_defect(self):
        """Check mode at create slug_name."""
        
        slug_name = slugify(self.city_name)
        self.assertEquals(slug_name, self.city.slug_name)

    def test_city_inactive_a_delete(self):
        """Check state inactive at delete."""

        id_city = self.city.id
        self.city.delete()
        state = City.objects.get(pk=id).active

        self.assertFalse(state.active)
