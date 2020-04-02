"""Cities managers."""

# Django 
from django.db import models

# Managers
from apps.utils.managers import SlugNameCreateManager

class CityManager(SlugNameCreateManager):
    """City manager.
    
    Used to handle code creation and add slug name by defect.
    """