from django.shortcuts import render
from django.http import HttpResponse   # added

# Create your views here.
def home(request):
    return render(request, 'base.html')
def main(request):
    return render(request, 'moodMatch/example.html')
