from django.db import models

from GamesPlay.core.validators import age_validator


class Profile(models.Model):
    email = models.EmailField(
        blank=False,
    )
    age = models.IntegerField(
        validators=[age_validator, ],
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=30,
        blank=False
    )
    first_name = models.CharField(
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        blank=True
    )
    profile_picture = models.URLField(
        blank=True,
    )
