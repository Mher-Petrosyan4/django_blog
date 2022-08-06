from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from helpers.choices import GenderChoice
from django.conf import settings


def profile_image_path(instance, filename):
    print(instance, filename)
    return f"profile_images/{instance.user.username}/{filename}"


class Profile(models.Model):
    profile_image = models.ImageField(upload_to=profile_image_path, default='static/images/profile_pic.png')
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(choices=GenderChoice.choices, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        obj = super().save(force_insert, force_update, using, update_fields)

        send_mail(
            subject="New Profile",
            message="For you new profile is created",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email]
        )