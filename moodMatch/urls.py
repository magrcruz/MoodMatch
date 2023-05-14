# films/urls.py
from django.urls import path
from . import views

app_name = 'moodMatch'
urlpatterns = [
    path('', views.index, name='index'),
    path('choose_emotion', views.choose_emotion, name='choose_emotion'),
    path('recommendation_results', views.recommendation_results, name='recommendation_results'),
    path('choose_content', views.choose_content, name='choose_content'),
    path('genre_preferences', views.choose_content, name='genre_preferences'),
    path('show_info', views.show_info, name='show_info'),
]