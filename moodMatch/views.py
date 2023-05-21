from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'moodMatch/index.html')

@login_required
def logout(request):
    return HttpResponse("logout")

@login_required
def choose_emotion(requet):
    return HttpResponse("Como te sientes hoy? Elige una emocion xd")

@login_required
def recommendation_results(request, type):
    return HttpResponse("Resultados de recomendaciones")

@login_required
def choose_content(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        # Realiza acciones con el valor recibido
        return redirect(reverse("moodMatch:recommendation_results", args=[type]))
    return render(request, 'moodMatch/choose_content.html')

@login_required
def genre_preferences(request):
    return HttpResponse("Elija genero")

def show_info(request):
    return HttpResponse("Info que debes conocer")