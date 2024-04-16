from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True, default="/home/dell/Desktop/socialmedia/media/posts/vit-c.jpg")

    def __str__(self):
        return self.user.username