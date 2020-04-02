"""Abstract person user model."""

# Django
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

# Utilities
from utils.models import BaseModel

# Models
from apps.locations.models import City
from apps.persons.models import Person


DEFAULT_TYPE_ADDRESS = "Residence"

TYPE_ADDRESS_CHOICES = (
    (DEFAULT_TYPE_ADDRESS, DEFAULT_TYPE_ADDRESS), 
)

class Address(BaseModel, models.Model):
    """Address model.

    Model at representing a address.
    """
    
    street = models.CharField('calle', max_length=50)
    number_street = models.CharField('número', max_length=18)
    floor = models.CharField('piso', max_length=18, null=True, blank=True)
    departament = models.CharField('departamento', max_length=18, null=True, blank=True)

    type_address = models.CharField(
        'tipo de residencia', 
        max_length=12, 
        choices=TYPE_ADDRESS_CHOICES, 
        default=DEFAULT_TYPE_ADDRESS
    )

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='ciudad')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        ordering = ['street', 'number_street']
        verbose_name = "dirección"
        verbose_name_plural = "direcciones"

    def get_absolute_url(self):
        """Returns the url to access a particular city instance."""
        return ""#reverse_lazy('article-detail', args=[str(self.id)])
    
    @property
    def full_address(self):
        return '{} {}'.format(self.street, self.number_street)

    def __str__(self):
        return self.full_address

