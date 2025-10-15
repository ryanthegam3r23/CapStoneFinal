from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Stat(models.Model):
    player = models.CharField(max_length=200)
    match = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    value = models.IntegerField()
    content = models.TextField()


    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player