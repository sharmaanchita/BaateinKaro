from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    user = instance
    
    if created:
        Profile.objects.create(
            user = user,
        )
        
@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()