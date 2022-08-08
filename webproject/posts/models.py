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
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return str(self.user)

    @property
    def num_like(self):
        return str.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

    def __str__(self):
        return str(self.post)
