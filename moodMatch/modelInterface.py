from .modelsRecomendation import Content, Emotion
from .models import UserPreferences
import random

def generate_recommendation(request,num_words, type, emotion):
    
    emotion = Emotion.objects.get(name=emotion)

    # Obtener las preferencias de género del usuario
    user_preferences = UserPreferences.objects.get(user=request.user)

    # Obtener los géneros preferidos del usuario
    genres_preferred = user_preferences.genres_preferences.all()

    # Consulta la base de datos para obtener las instancias que cumplan con las características
    recommendations = Content.objects.filter(
        type=type,
        emotion = emotion,
        genre__in=genres_preferred
    ).order_by('?')

    return list(recommendations)[:num_words]