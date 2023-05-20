from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView

from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'  # Especifica el nombre de tu plantilla personalizada de inicio de sesión
    success_url = '/'  # Especifica la URL a la que se redirigirá después del inicio de sesión exitoso
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"