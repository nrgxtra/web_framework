# Generated by Django 4.0.4 on 2022-04-18 07:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2, 'must be at least 2 characters long')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
