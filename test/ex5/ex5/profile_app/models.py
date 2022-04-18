from django.core.validators import MinLengthValidator
from django.db import models

from ex5.core.validators import username_validation


class Profile(models.Model):
    username = models.CharField(
        validators=[
            MinLengthValidator(2),
            username_validation,
        ],
        blank=False,
        max_length=15,

    )
    email = models.EmailField(
        blank=False,
    )
    age = models.PositiveIntegerField()

