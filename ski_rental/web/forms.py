# web/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nombre...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'contraseña...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirma contraseña...'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']