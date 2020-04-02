"""Abstract person model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from utils.models import BaseModel


class AbstractPerson(BaseModel, models.Model):
    """Abstrat person model.

    """

    id_card = models.CharField('DNI', max_length=30, unique=True)
    first_name = models.CharField('nombres', max_length=210)
    last_name = models.CharField('apellido', max_length=210)
    birth_date = models.DateField('fecha de nacimiento', null=True, blank=True)
    biography = models.TextField('biography', max_length=1200, null=True, blank=True)
    
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone numbermust be entered in the format: +99999999. Up to 15 digits allowed.'
    )

    movile_number = models.CharField(
        'celular',
        validators=[phone_regex,], 
        max_length=17, 
        null=True, 
        blank=True
    )

    telephone_number = models.CharField(
        'teléfono', 
        validators=[phone_regex,],
        max_length=17, 
        null=True, 
        blank=True
    )

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        abstract = True
        ordering = ['last_name', 'first_name']
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        """Return full name"""
        return self.full_name

