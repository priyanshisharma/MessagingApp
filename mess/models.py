from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    author = models.CharField(max_length=200,default="Anonymous")
    