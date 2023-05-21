from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .modelInterface import generate_recommendation

numRecommendations = 5
# Create your views here.
def index(request):
    return render(request, 'moodMatch/index.html')

@login_required
def logout(request):
    return HttpResponse("logout")

@login_required
def choose_emotion(request, type):
    if request.method == 'POST':
        emotion = request.POST.get('emotion')
        # Realiza acciones con el valor recibido
        return redirect(reverse("moodMatch:recommendation_results", args=[type,emotion]))
    return render(request, 'moodMatch/choose_emotion.html')

@login_required
def recommendation_results(request, type, emotion):
    recomendation = generate_recommendation(numRecommendations, type, emotion)
    
    context = {
        'recommendations_results': recomendation
    }
    
    return render(request, 'moodMatch/recommendation_results.html', context)


@login_required
def choose_content(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        # Realiza acciones con el valor recibido
        return redirect(reverse("moodMatch:choose_emotion", args=[type]))
    return render(request, 'moodMatch/choose_content.html')

@login_required
def genre_preferences(request):
    return HttpResponse("Elija genero")

def show_info(request):
    return HttpResponse("Info que debes conocer")