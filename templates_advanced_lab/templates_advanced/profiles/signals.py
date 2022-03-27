from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(**kwargs):
    pass
