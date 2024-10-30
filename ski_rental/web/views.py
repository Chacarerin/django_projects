# web/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from .forms import ClienteRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Equipo, Categoria, Arriendo
from django.utils import timezone
from django import forms
from django.db.models import Count
from django.contrib import messages


def index(request):
    # Filtrar equipos que están disponibles para arrendar
    equipos_disponibles = Equipo.objects.filter(estado='disponible')
    categorias = Categoria.objects.all()
    total_equipos = equipos_disponibles.count()  # Cuenta de equipos disponibles
    return render(request, 'index.html', {
        'equipos': equipos_disponibles,
        'categorias': categorias,
        'total_equipos': total_equipos
    })


def register(request):
    if request.method == 'POST':
        form = ClienteRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            cliente_group = Group.objects.get(name='Cliente')
            user.groups.add(cliente_group)  # Asigna el usuario al grupo Cliente
            login(request, user)
            return redirect('/')  # Redirige a la página principal después del registro
    else:
        form = ClienteRegisterForm()
    return render(request, 'register.html', {'form': form})
        

def is_operario(user):
    return user.groups.filter(name='Operario').exists()

@login_required
def listar_arriendos(request):
    # Consulta todos los arriendos
    arriendos = Arriendo.objects.all()
    
    # Verifica si el usuario es operario
    es_operario = request.user.groups.filter(name='Operario').exists()
    
    # Procesar la observación solo si es operario y se ha enviado una observación
    if es_operario and request.method == 'POST':
        arriendo_id = request.POST.get('arriendo_id')
        comentario = request.POST.get('comentario')
        if arriendo_id and comentario:
            arriendo = Arriendo.objects.get(id=arriendo_id)
            arriendo.observacion = comentario
            arriendo.save()
            return redirect('listar_arriendos')

    # Renderiza la lista de arriendos y si el usuario es operario
    return render(request, 'listar_arriendos.html', {
        'arriendos': arriendos,
        'es_operario': es_operario
    })

class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['fecha', 'observacion']

@login_required
def arrendar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        form = ArriendoForm(request.POST)
        if form.is_valid():
            arriendo = form.save(commit=False)
            arriendo.user = request.user
            arriendo.equipo = equipo
            equipo.estado = 'arrendado'  # Cambiar el estado del equipo
            equipo.save()
            arriendo.save()
            return redirect('index')
    else:
        form = ArriendoForm()
    return render(request, 'arrendar_equipo.html', {'form': form, 'equipo': equipo})

# Esto asegura la protección CSRF
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Has salido correctamente.")
        return redirect('index')
    return redirect('index')  # En caso de acceso GET, redirige a la página principal