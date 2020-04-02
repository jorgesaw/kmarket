"""Person model."""

# Django
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

# Utilities
from utils.models import BaseModel

# Models
from apps.persons.models import AbstractPerson

class Person(AbstractPerson):
    """Person model.
    
    Representing a person with addresses
    """
    pass

