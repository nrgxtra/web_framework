from django.db import models

from GamesPlay.core.validators import rating_validator, max_level_validator


class Game(models.Model):
    title = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
    )
    CHOICES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )
    category = models.CharField(
        max_length=15,
        choices=CHOICES,
        blank=False,
    )
    rating = models.FloatField(
        validators=[rating_validator, ],
        blank=False,
        null=False,

    )
    max_level = models.IntegerField(
        validators=[max_level_validator, ],
        blank=False,
    )
    image_url = models.URLField(
        blank=False,
    )
    summary = models.TextField(
        blank=True,
    )
