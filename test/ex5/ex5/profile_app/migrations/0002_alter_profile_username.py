# Generated by Django 4.0.4 on 2022-04-18 08:13

import django.core.validators
from django.db import migrations, models
import ex5.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), ex5.core.validators.username_validation]),
        ),
    ]
