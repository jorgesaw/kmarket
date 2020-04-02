"""City model."""

# Django
from django.db import models
from django.urls import reverse_lazy

# Managers
from apps.locations.managers import CityManager

# Models
from .states import State

# Mixins
from apps.utils.models_mixin import ModelWithSlugNameMixin

# Utilities
from apps.utils.models import BaseModel
from django.utils.text import slugify


class City(ModelWithSlugNameMixin, BaseModel):
    """Model representing a city."""
    
    name = models.CharField('nombre', max_length=70, unique=True)
    
    slug_name = models.CharField(
        'slug name', 
        max_length=70, 
        unique=True, 
        blank=True, 
        help_text="Slug name",
    )

    zip_city = models.CharField('código postal', max_length=30, null=True, blank=True)
    ddn = models.CharField('característica', max_length=12, null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name',]
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"

    def __str__(self):
        """Return name."""
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(City, self).save(*args, **kwargs)
