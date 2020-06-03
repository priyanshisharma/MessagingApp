from django.db import models

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    author = models.CharField(max_length=200)
