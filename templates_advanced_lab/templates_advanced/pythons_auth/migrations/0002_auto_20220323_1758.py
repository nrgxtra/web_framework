# Generated by Django 3.1.3 on 2022-03-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythons_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythonuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pythonuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
