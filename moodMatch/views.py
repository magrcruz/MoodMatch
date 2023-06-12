from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .modelInterface import generate_recommendation
from .models import *

numRecommendations = 5
def is_premium(request):
    user={
        "is_premium": request.user in SubscriptionNotification.objects.get(id=2).users.all()
    }
    return user

# Create your views here.
def index(request):
    return render(request, 'moodMatch/index.html')

@login_required
def logout(request):
    return HttpResponse("logout",{"user":is_premium(request)})

@login_required
def choose_emotion(request, type):
    if request.method == 'POST':
        emotion = request.POST.get('type')
        # Realiza acciones con el valor recibido
        return redirect(reverse("moodMatch:recommendation_results", args=[type,emotion]))
    return render(request, 'moodMatch/choose_emotion.html',{"user":is_premium(request)})

@login_required
def recommendation_results(request, type, emotion):
    recomendation, left = generate_recommendation(request,numRecommendations, type, emotion)
    
    context = {
        'count_recommendations':left,
        'recommendations_results': recomendation,
        "user":is_premium(request)
    }
    
    return render(request, 'moodMatch/recommendation_results.html', context)


@login_required
def choose_content(request):
    if request.method == 'POST':
        content_type = request.POST.get('type')
        if content_type != "song":
            return redirect(reverse("moodMatch:working"))
        #elif
        # Realiza acciones con el valor recibido
        return redirect(reverse("moodMatch:choose_emotion", args=[content_type]))
    return render(request, 'moodMatch/choose_content.html',{"user":is_premium(request)})

@login_required
def genre_preferences(request):
    s_genres = Genre.objects.filter(type='song')
    f_genres = Genre.objects.filter(type='film')

    if request.method == 'POST':
        selected_song_genres = request.POST.getlist('song_genres') 
        selected_film_genres = request.POST.getlist('film_genres')
        
        # Guardar preferencias
        user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)

        # Obtener géneros seleccionados previamente
        selected_songs = user_preferences.genres_preferences.filter(type='song')
        selected_films = user_preferences.genres_preferences.filter(type='film')

        # Agregar géneros seleccionados actualmente
        for genre_id in selected_song_genres:
            genre = Genre.objects.get(id=genre_id)
            if genre not in selected_songs:
                user_preferences.genres_preferences.add(genre)
        
        for genre_id in selected_film_genres:
            genre = Genre.objects.get(id=genre_id)
            if genre not in selected_films:
                user_preferences.genres_preferences.add(genre)

        # Eliminar géneros deseleccionados
        for genre in selected_songs:
            if str(genre.id) not in selected_song_genres:
                user_preferences.genres_preferences.remove(genre)
        
        for genre in selected_films:
            if str(genre.id) not in selected_film_genres:
                user_preferences.genres_preferences.remove(genre)

        return redirect(reverse("moodMatch:choose_content"))

    try:
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        # Si no existe un objeto UserPreferences, crear uno nuevo
        user_preferences = UserPreferences.objects.create(user=request.user)

    selected_songs = user_preferences.genres_preferences.filter(type='song')
    selected_films = user_preferences.genres_preferences.filter(type='film')

    # Agregar campo adicional 'isSelected'
    song_genres = [
        {'genre': genre, 'isSelected': genre in selected_songs}
        for genre in s_genres
    ]
    film_genres = [
        {'genre': genre, 'isSelected': genre in selected_films}
        for genre in f_genres
    ]

    return render(request, 'moodMatch/genre_preferences.html', {'song_genres': song_genres, 'film_genres': film_genres,"user":is_premium(request)})

def show_info(request):
    return render(request, 'moodMatch/show_info.html')

@login_required
def working(request):
    user = request.user
    subscription = SubscriptionNotification.objects.get(id=1)
    register = False
    if request.method == 'POST':
        register = True
        if not user in subscription.users.all():
            subscription.users.add(user)
    elif user in subscription.users.all():
            register = True

    return render(request, 'moodMatch/working.html', {'register': register,"user":is_premium(request)})