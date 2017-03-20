from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    website = models.URLField(max_length=50,blank=True,)
    phonenumber = models.IntegerField(null=True)
