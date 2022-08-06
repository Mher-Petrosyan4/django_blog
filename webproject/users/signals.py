from users.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_profile(instance, created, sender, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("##### profile is created")


post_save.connect(receiver=create_profile, sender=User)
