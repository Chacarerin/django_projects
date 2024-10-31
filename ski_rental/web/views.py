from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import RegistroForm
from .models import Equipo, Categoria, Arriendo
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.http import HttpResponseForbidden

def index(request):
    categoria_id = request.GET.get('categoria')
    equipos = Equipo.objects.filter(estado='disponible')
    
    # Filtrar por categoría si está seleccionada
    if categoria_id:
        equipos = equipos.filter(categoria_id=categoria_id)

    # Obtener todas las categorías para el filtro
    categorias = Categoria.objects.all()
    
    
    return render(request, 'index.html', {
        'equipos': equipos,
        'categorias': categorias,
    })

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'La sesión se ha cerrado correctamente.')
    return redirect('login')  # Redirigir al login después de cerrar sesión

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Cambia 'home' por la ruta de inicio que prefieras
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login')
def arrendar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id, estado='disponible')
    hoy = date.today()  # Fecha actual

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        
        # Validar que la fecha seleccionada no sea anterior a hoy
        if fecha and fecha >= str(hoy):
            # Crear el arriendo y actualizar el estado del equipo
            arriendo = Arriendo(user=request.user, equipo=equipo, fecha=fecha)
            arriendo.save()
            equipo.estado = 'arrendado'
            equipo.save()
            messages.success(request, f'Has arrendado el equipo {equipo.nombre} exitosamente.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, selecciona una fecha válida.')

    return render(request, 'arrendar.html', {'equipo': equipo, 'hoy': hoy})

@login_required
def lista_arriendos(request):
    # Solo permite acceso si el usuario es un operario
    if request.user.userprofile.tipo != 'operario':
        return HttpResponseForbidden("No tienes permiso para ver esta página.")
    
    arriendos = Arriendo.objects.select_related('equipo', 'user')
    return render(request, 'lista_arriendos.html', {'arriendos': arriendos})

@login_required
def agregar_observacion(request, arriendo_id):
    if request.user.userprofile.tipo != 'operario':
        return HttpResponseForbidden("No tienes permiso para realizar esta acción.")
    
    arriendo = get_object_or_404(Arriendo, id=arriendo_id)
    if request.method == 'POST':
        observacion = request.POST.get('observacion')
        if observacion:
            arriendo.observacion = observacion
            arriendo.save()
            messages.success(request, 'Observación guardada exitosamente.')
    return redirect('lista_arriendos')

@login_required
def marcar_danado(request, arriendo_id):
    if request.user.userprofile.tipo != 'operario':
        return HttpResponseForbidden("No tienes permiso para realizar esta acción.")
    
    arriendo = get_object_or_404(Arriendo, id=arriendo_id)
    if request.method == 'POST':
        arriendo.danado = 'danado' in request.POST
        arriendo.save()
        messages.success(request, 'Estado de daño actualizado.')
    return redirect('lista_arriendos')