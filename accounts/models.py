from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(default='default.webp', upload_to='avatars')


class Subscriber(models.Model):
    email = models.EmailField(max_length=30)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.email
