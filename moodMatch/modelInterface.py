from .modelsRecomendation import Content, Emotion
import random

def generate_recommendation(num_words, type, emotion):
    
    emotion = Emotion.objects.get(name=emotion)

    # Consulta la base de datos para obtener las instancias que cumplan con las características
    recommendations = Content.objects.filter(
        type=type,
        emotions__id=emotion.id,
    )

    return list(recommendations)[:num_words]