from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(default='default_avatar.png', upload_to='avatars')


class Subscriber(models.Model):
    email = models.EmailField(max_length=30)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
