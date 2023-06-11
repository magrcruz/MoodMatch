from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(Content)
admin.site.register(Emotion)
admin.site.register(UserRecomendations)
admin.site.register(SubscriptionNotification)