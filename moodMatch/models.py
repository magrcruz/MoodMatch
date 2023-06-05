from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta

from .modelsRecomendation import *
# Create your models here.

dailyRecommendations = 5

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genres_preferences = models.ManyToManyField(Genre)

class UserRecomendations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totalRecomendations = models.IntegerField(default=0)
    recomendationsleft = models.IntegerField(default=0)
    lastTimeRecharged = models.DateField(default=timezone.now().date() - timezone.timedelta(days=1))

    def has_recommendations(self):
        return self.recomendationsleft
    
    def can_recharge(self):
        if self.recomendationsleft>0: return False
        current_date = datetime.now().date()
        time_difference = current_date - self.lastTimeRecharged
        return time_difference.days >= 1
    
    def recharge(self):
        self.recomendationsleft += dailyRecommendations
        self.lastTimeRecharged = datetime.now().date()
        self.save()

    def use_recomendation(self):
        self.recomendationsleft -= 1
        self.totalRecomendations += 1
        self.save()

class SubscriptionNotification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User)