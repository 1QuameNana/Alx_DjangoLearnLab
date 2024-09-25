
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(max_length=200, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)
# Create your models here.
