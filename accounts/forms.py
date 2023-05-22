from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre',"class":"form-control"}))
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario',"class":"form-control"})
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo',"class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña',"class":"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']