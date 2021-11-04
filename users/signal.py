from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance: User, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)
