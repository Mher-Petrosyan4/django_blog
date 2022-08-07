import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


def profile_image_path(instance, filename):
    print(instance, filename)
    return f"posts_images/{instance.user.username}/{filename}"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to=profile_image_path, blank=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

# def profile_image_path(instance, filename):
#     print(instance, filename)
#     return f"profile_images/{instance.user.username}/{filename}"
#
#
# class Profile(models.Model):
#     profile_image = models.ImageField(upload_to=profile_image_path, default='static/images/profile_pic.png')
#     bio = models.TextField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     gender = models.IntegerField(choices=GenderChoice.choices, blank=True, null=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)