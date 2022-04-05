from django.db import models


class Cat(models.Model):
    name = models.CharField(
        max_length=15,
    )

    age = models.IntegerField()

