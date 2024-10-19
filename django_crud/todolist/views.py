from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required, permission_required
from .models import Tarea, Visitas
from .forms import TareaForm
from .forms import RegistroForm
from django.http import HttpResponseForbidden

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Asignar el permiso "editor_access" directamente al usuario
            permiso_editor = Permission.objects.get(codename='editor_access')
            user.user_permissions.add(permiso_editor)

            login(request, user)  # Autenticar al usuario después del registro
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

def lista_tareas(request):
    tareas = Tarea.objects.all()  # Obtener todas las tareas de la base de datos
    visitas_obj, created = Visitas.objects.get_or_create(id=1)
        # Incrementar el contador de visitas
    visitas_obj.contador += 1
    visitas_obj.save()
    
    # Comprobar si el usuario tiene el permiso 'editor_access'
    user_is_editor = request.user.has_perm('todolist.editor_access')

    return render(request, 'lista_tareas.html', {
        'tareas': tareas,
        'visitas': visitas_obj.contador,
        'user_is_editor': user_is_editor  # Pasar esta variable a la plantilla
    })

# Vista para agregar tarea (solo permitido para "editor")
@login_required
@permission_required('todolist.editor_access', raise_exception=True)
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user  # Asigna la tarea al usuario que está autenticado
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'agregar_tarea.html', {'form': form})

# Vista para editar tarea (solo permitido para "editor" y el propietario de la tarea)
@login_required
@permission_required('todolist.editor_access', raise_exception=True)
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)

    # Verificar que la tarea pertenezca al usuario que la intenta editar
    if tarea.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para editar esta tarea.")

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'editar_tarea.html', {'form': form, 'tarea': tarea})

# Vista para eliminar tarea (solo permitido para "editor" y el propietario de la tarea)
@login_required
@permission_required('todolist.editor_access', raise_exception=True)
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)

    # Verificar que la tarea pertenezca al usuario que la intenta eliminar
    if tarea.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta tarea.")

    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')

    return render(request, 'eliminar_tarea.html', {'tarea': tarea})