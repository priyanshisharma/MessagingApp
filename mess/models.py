from django.db import models
from django.conf import settings

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    author = models.CharField(max_length=200)
    #is_anonymous = models.BooleanField(default=True)    
