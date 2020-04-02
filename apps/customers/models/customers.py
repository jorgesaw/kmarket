"""Customer model."""

# Django
from django.db import models

# Utilities
from apps.persons.models import Person

class Customer(Person):
    """Customer model."""

    class Meta(Person.Meta):
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

