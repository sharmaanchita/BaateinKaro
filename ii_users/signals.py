from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    user = instance
    
    if created:
        Profile.objects.create(
            user = user,
        )
    else:
        # update allauth emailaddress if exists 
        try:
            email_address = EmailAddress.objects.get_primary(user)
            if email_address.email != user.email:
                email_address.email = user.email
                email_address.verified = False
                email_address.save()
        except:
            # if allauth emailaddress doesn't exist create one
            EmailAddress.objects.create(
                user = user,
                email = user.email, 
                primary = True,
                verified = False
            )
        
@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()