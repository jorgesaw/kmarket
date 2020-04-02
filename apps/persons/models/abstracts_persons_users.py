"""Abstract person user model."""

# Django
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

# Utilities
from utils.models import BaseModel

# Models
from apps.persons.models import AbstractPerson
from apps.users.models import User


class AbstractPersonUser(AbstractPerson):
    """Abstract person user model. 

    Model representing a person with user. 
    When saving the person's data, a user is created.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = User(username=self.id_card)
        user.set_password(self.id_card)
        user.save()
        self.user = user
        super(AbstractPerson, self).save(*args, **kwargs)
