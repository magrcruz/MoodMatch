from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'  # Especifica el nombre de tu plantilla personalizada de inicio de sesión
    success_url = '/'  # Especifica la URL a la que se redirigirá después del inicio de sesión exitoso

class SignUpView(generic.CreateView):
    model = User
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("choose_preferences")

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect(reverse("moodMatch:genre_preferences"))
    
    def form_invalid(self, form):
        print("Ocurrió un error durante la creación del usuario.")
        print("Errores del formulario:", form.errors)
        return super().form_invalid(form)