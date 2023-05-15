from django.shortcuts import render
from django.http import HttpResponse   # added
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'moodMatch/example.html')

@login_required
def logout(request):
    return HttpResponse("logout")

@login_required
def choose_emotion(requet):
    return HttpResponse("Como te sientes hoy? Elige una emocion xd")

@login_required
def recommendation_results(request):
    return HttpResponse("Resultados de recomendaciones")

@login_required
def choose_content(request):
    return HttpResponse("Elija entre muscia peli o serie")

@login_required
def genre_preferences(request):
    return HttpResponse("Elija genero")

def show_info(request):
    return HttpResponse("Info que debes conocer")