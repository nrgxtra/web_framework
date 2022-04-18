from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        blank=False,
        null=False,
    )
    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    TYPE_CHOICE_POP = 'Pop Music'
    TYPE_CHOICE_JAZZ = 'Jazz Music'
    TYPE_CHOICE_RnB = 'R&B Music'
    TYPE_CHOICE_ROCK = 'Rock Music'
    TYPE_CHOICE_COUNTRY = 'Country Music'
    TYPE_CHOICE_DANCE = 'Dance Music'
    TYPE_CHOICE_HI_HOP = 'Hip Hop Music'
    TYPE_CHOICE_OTHER = 'Other'
    TYPE_CHOICES = (
        (TYPE_CHOICE_POP, 'Pop Music'),
        (TYPE_CHOICE_JAZZ, 'Jazz Music'),
        (TYPE_CHOICE_RnB, 'R&B Music'),
        (TYPE_CHOICE_ROCK, 'Rock Music'),
        (TYPE_CHOICE_COUNTRY, 'Country Music'),
        (TYPE_CHOICE_DANCE, 'Dance Music'),
        (TYPE_CHOICE_HI_HOP, 'Hip Hop Music'),
        (TYPE_CHOICE_OTHER, 'Other'),
    )

    genre = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
    )
    description = models.TextField()
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        validators=[MinValueValidator(0)],
        blank=False,
        null=False,
    )
