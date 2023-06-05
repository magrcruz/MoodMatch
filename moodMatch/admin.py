from django.contrib import admin
from .models import Genre, Content, Emotion

# Register your models here.
admin.site.register(Genre)
admin.site.register(Content)
admin.site.register(Emotion)