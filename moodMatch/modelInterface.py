from .modelsRecomendation import Content, Emotion, Genre
from .models import UserPreferences, UserRecomendations, SubscriptionNotification
import random


def generate_recommendation(request,num_words, type, emotion):
    
    # Verificar que tiene intentos disponibles
    user_recomendations, created = UserRecomendations.objects.get_or_create(user=request.user, defaults={'totalRecomendations': 0, 'recomendationsleft': 0})
    
    if user_recomendations.can_recharge():
        user_recomendations.recharge()
    
    if not user_recomendations.has_recommendations():
        if not request.user in SubscriptionNotification.objects.get(id=2).users.all():
            return [],0
        else:
            user_recomendations.recharge()

    emotion = Emotion.objects.get(name=emotion)

    # Obtener las preferencias de género del usuario
    user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)

    # Obtener los géneros preferidos del usuario
    genres_preferred = user_preferences.genres_preferences.all()
    if not genres_preferred:
        # Si el usuario no tiene preferencias, asigna todos los géneros disponibles
        genres_preferred = Genre.objects.all()
    
    # Consulta la base de datos para obtener las instancias que cumplan con las características
    recommendations = Content.objects.filter(
        type=type,
        emotion = emotion,
        genre__in=genres_preferred
    ).order_by('?')
    if len(list(recommendations)):
        user_recomendations.use_recomendation()
    return list(recommendations)[:num_words],user_recomendations.has_recommendations()