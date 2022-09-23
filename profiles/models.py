from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    about_me = models.TextField(null=True)
    photo = models.TextField(null=True)
    last_seen = models.DateTimeField(auto_now=True)


class OnLineUsers(models.Model):
    logged = models.OneToOneField(User, on_delete=models.CASCADE)


