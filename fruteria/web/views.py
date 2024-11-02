from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

@login_required
@user_passes_test(lambda u: u.userprofile.tipo == 'administrador')
def ventas(request):
    return render(request, 'ventas.html')

@login_required
@user_passes_test(lambda u: u.userprofile.tipo == 'administrador')
def stock(request):
    return render(request, 'stock.html')

def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Crea el usuario y el perfil con tipo "cliente"
            messages.success(request, "Registro exitoso. Por favor, inicia sesión.")
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect("login")  # Redirigir a la página de login al cerrar sesión

@login_required
def home(request):
    return render(request, "index.html")  # Página de inicio protegida