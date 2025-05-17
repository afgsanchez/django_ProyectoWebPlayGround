from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    # Custom upload path for the avatar
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()  # Delete the old file
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

    # def __str__(self):
    #     return self.username

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # Create a Profile instance for the new User
        # This will create a Profile instance if it doesn't exist
        Profile.objects.get_or_create(user=instance)
        print("Profile created for user:", instance.username)
