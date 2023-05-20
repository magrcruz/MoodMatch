from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))
