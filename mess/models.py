from django.db import models

# Create your models here.

class Message(models.Model):
    is_anonymous = models.BooleanField(default=False)
    text = models.TextField()
    if(is_anonymous):
        author = models.CharField(default="Anonymous")
    else
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)