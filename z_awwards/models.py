from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """
    User Profile model
    """
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    username = models.TextField(max_length=150)
    bio = models.TextField(max_length=500, blank=True, default="default bio")
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/profile_pic/', blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return f'{self.user.username}: profile'

