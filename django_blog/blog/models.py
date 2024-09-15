from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.conf import settings


class Posts(models.Model):
    title = models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)