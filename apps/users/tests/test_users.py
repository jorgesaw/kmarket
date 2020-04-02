"""Users tests."""

# Django REST Framework
from rest_framework.test import APITestCase

# Models
from apps.users.models import User

class UserAccountTest():
    """Ensure account at users account."""

    def setUp(self):
        """Test case setup."""

        self.user = User.objects.create(
            first_name='Jorge Adrián',
            last_name='Gonzalez',
            email='jag@kubelk.com', 
            username='jag', 
            password='kilLO677QW'
        )

    def test_profile_create(self):
        """If exists profile at create user."""

        self.assertIsNone(self.user.profile)