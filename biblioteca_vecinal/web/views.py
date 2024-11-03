from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from .models import Libro, Categoria


@login_required
def book_list(request):
    # Obtener todas las categorías para el filtro
    categorias = Categoria.objects.all()
    
    # Filtrar libros por categoría seleccionada (si existe)
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        libros = Libro.objects.filter(categoria_id=categoria_id)
    else:
        libros = Libro.objects.all()

    context = {
        'libros': libros,
        'categorias': categorias,
    }
    return render(request, 'index.html', context)

# Vista de registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Vista de login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido, {user.first_name}!")
                return redirect('index')  # Redirige a la página principal después del login
        messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista de logout
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect('login')