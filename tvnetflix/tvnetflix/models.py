from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    cat1 = models.CharField(max_length = 100)
    cat1_score = models.IntegerField()

    
