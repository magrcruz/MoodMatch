from django.shortcuts import render
from django.http import HttpResponse   # added

# Create your views here.
def index(request):
    return HttpResponse("Pagina principal")

def login(request):
    return HttpResponse("login")

def signup(request):
    return HttpResponse("signup")

def choose_emotion(requet):
    return HttpResponse("Como te sientes hoy? Elige una emocion xd")

def recommendation_results(request):
    return HttpResponse("Resultados de recomendaciones")

def choose_content(request):
    return HttpResponse("Elija entre muscia peli o serie")

def genre_preferences(request):
    return HttpResponse("Elija genero")

def show_info(request):
    return HttpResponse("Info que debes conocer")