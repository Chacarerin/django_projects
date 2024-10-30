from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio, Producto
from .forms import LaboratorioForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    
    # Contador de visitas
    if 'visitas' in request.session:
        request.session['visitas'] += 1
    else:
        request.session['visitas'] = 1
    
    return render(request, 'lista_laboratorios.html', {'laboratorios': laboratorios})


def agregar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'agregar_laboratorio.html', {'form': form})


def editar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form, 'laboratorio': laboratorio})


def eliminar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('lista_laboratorios')
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})


# Registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

# Login de usuarios
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})