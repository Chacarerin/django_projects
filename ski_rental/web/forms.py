from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'nombre...'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'nombre de usuario...'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'contraseña...'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'confirmar contraseña...'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
            # Crear un perfil de usuario con el tipo 'cliente' por defecto
            UserProfile.objects.create(user=user, tipo='cliente')
        return user