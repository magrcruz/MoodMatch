from django.db import models
from django.contrib.auth.models import User

from .modelsRecomendation import *
# Create your models here.

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres_preferences = models.ManyToManyField(Genre)