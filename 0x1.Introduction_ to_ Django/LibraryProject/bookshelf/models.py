from django.db import models

# Create your models here.
class Book(models.Model):
    title =models.CharField(max_length =200, null =False)
    author = models.CharField(max_length = 200,null= False)
    Publication_year = models.IntegerField(null=False)