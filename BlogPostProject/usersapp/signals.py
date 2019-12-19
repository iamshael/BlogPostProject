from django.db.models.signals import post_save # after suer creation
from django.contrib.auth.models import User #sender
from django.dispatch import receiver #receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profie(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_profie(sender, instance, **kwargs):
    instance.profile.save()
