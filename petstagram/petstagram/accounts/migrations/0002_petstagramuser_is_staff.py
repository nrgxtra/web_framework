# Generated by Django 4.0.3 on 2022-03-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petstagramuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
