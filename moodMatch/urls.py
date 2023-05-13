# films/urls.py
from django.urls import path
from . import views

app_name = 'moodMatch'
urlpatterns = [
    path('', views.main, name='main'),
]