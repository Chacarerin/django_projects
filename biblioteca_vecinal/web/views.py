from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from .models import Libro, Categoria, Prestamo
from datetime import datetime 
from django.utils import timezone


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

@login_required
def mis_arriendos(request):
    # Obtener los libros arrendados por el usuario actual
    prestamos = Prestamo.objects.filter(usuario=request.user, activo=True)
    context = {
        'prestamos': prestamos,
    }
    return render(request, 'mis_arriendos.html', context)

@login_required
def arrendar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    # Verificar si hay ejemplares disponibles
    if libro.cantidad_disponible < 1:
        messages.error(request, f'El libro "{libro.titulo}" no está disponible para arriendo.')
        return redirect('index')

    if request.method == 'POST':
        # Obtener fecha de préstamo como string desde el formulario y convertirla a datetime
        fecha_prestamo_str = request.POST.get('fecha_prestamo')
        fecha_prestamo = datetime.strptime(fecha_prestamo_str, "%Y-%m-%d")
        fecha_prestamo = timezone.make_aware(fecha_prestamo)  # Asegurar que sea timezone-aware

        # Calcular fecha de devolución esperada como timezone-aware datetime
        fecha_devolucion_esperada = fecha_prestamo + timedelta(days=libro.tipo.dias_prestamo)
        
        # Crear el préstamo y reducir la cantidad disponible
        Prestamo.objects.create(
            usuario=request.user,
            libro=libro,
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion_esperada=fecha_devolucion_esperada,
            activo=True
        )
        libro.cantidad_disponible -= 1  # Reducir la cantidad disponible en 1
        libro.save()

        messages.success(request, f'Has arrendado el libro "{libro.titulo}" exitosamente.')
        return redirect('mis_arriendos')

    return render(request, 'arrendar.html', {'libro': libro})


@login_required
def retornar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    prestamo = get_object_or_404(Prestamo, libro=libro, usuario=request.user, activo=True)

    if request.method == 'POST':
        fecha_devolucion_real_str = request.POST.get('fecha_devolucion_real')
        
        # Convertir fecha_devolucion_real de string a datetime y hacerla timezone-aware
        fecha_devolucion_real = datetime.strptime(fecha_devolucion_real_str, "%Y-%m-%d")
        fecha_devolucion_real = timezone.make_aware(fecha_devolucion_real)

        prestamo.fecha_devolucion_real = fecha_devolucion_real
        prestamo.activo = False
        
        # Verificar que cantidad_disponible no supere cantidad_total
        if libro.cantidad_disponible < libro.cantidad_total:
            libro.cantidad_disponible += 1  # Aumentar la cantidad disponible en 1 solo si no se excede cantidad_total
        
        libro.save()

        # Convertir fecha_devolucion_esperada a timezone-aware si es necesario
        fecha_devolucion_esperada = prestamo.fecha_devolucion_esperada
        if timezone.is_naive(fecha_devolucion_esperada):
            fecha_devolucion_esperada = timezone.make_aware(fecha_devolucion_esperada)

        # Calcular los días de retraso usando timezone-aware datetime
        dias_retraso = (fecha_devolucion_real - fecha_devolucion_esperada).days

        if dias_retraso > 0:
            prestamo.multa_total = dias_retraso * libro.tipo.multa_dia_atraso
            messages.warning(request, f'El libro "{libro.titulo}" se retornó con {dias_retraso} días de retraso, generando ${prestamo.multa_total} en multa.')
        else:
            messages.success(request, f'Has retornado el libro "{libro.titulo}" sin retraso.')
        
        prestamo.save()
        return redirect('mis_arriendos')

    return render(request, 'retornar.html', {'libro': libro})