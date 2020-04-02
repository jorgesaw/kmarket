"""States tests."""

# Django
from django.test import TestCase

# Models
from apps.locations.models import State

# Utilities
from django.utils.text import slugify


class StateManagerTestCase(TestCase):
    """State manager statetest case."""

    def setUp(self):
        """Test case setup."""
    
        self.name_state = 'Santa Fé'
        self.state = State.objects.create(name=self.state_name)
        

    def test_slug_name_create(self):
        """if slug_name has created at save."""

        self.assertIsNone(self.state.slug_name)

    def test_slug_name_by_defect(self):
        """Check mode at create slug_name."""
        
        slug_name = slugify(self.state_name)
        self.assertEquals(slug_name, self.state.slug_name)

    def test_state_inactive_a_delete(self):
        """Check state inactive at delete."""

        id_state = self.state.id
        self.state.delete()
        state = State.objects.get(pk=id).active

        self.assertFalse(state.active)
