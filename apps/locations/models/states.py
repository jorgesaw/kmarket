"""State model."""

# Django
from django.db import models
from django.urls import reverse_lazy

# Managers
from apps.locations.managers import StateManager

# Mixins
from apps.utils.models_mixin import ModelWithSlugNameMixin

# Utilities
from apps.utils.models import BaseModel


class State(ModelWithSlugNameMixin, BaseModel):
    """State mode.

    Model representing a state.
    """
    
    name = models.CharField(
        'nombre', 
        max_length=70, 
        unique=True, 
        help_text="Nombre",
    )

    slug_name = models.CharField(
        'slug name', 
        max_length=70, 
        unique=True, 
        blank=True, 
        help_text="Slug name",
    )

    class Meta:
        ordering = ['name']
        verbose_name = "provincia"
        verbose_name_plural = "provincias"

    def __str__(self):
        """Return name."""
        return self.name
