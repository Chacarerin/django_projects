from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth import views as auth_views


def index(request):
    return render(request, 'index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  # Obtiene el producto o muestra error 404
    if request.method == 'POST':
        producto.delete()  # Elimina el producto
        return redirect('lista_productos')  # Redirige a la lista de productos después de eliminar
    return render(request, 'eliminar_producto.html', {'producto': producto})

# Vista que recibe un parámetro de cadena (username)
def mostrar_username(request, cadena):
    # Verificar si la cadena está vacía
    if cadena.strip():
        return HttpResponse(f"El username es: {cadena}")
    else:
        return HttpResponse("La cadena está vacía")
    
# Vista para mostrar el detalle de un producto individual
def detalle_producto(request, id):
    # Obtener el producto por su ID o devolver 404 si no existe
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})

# Vista para manejar el registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo usuario
            return redirect('login')  # Redirigir al inicio de sesión
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

# Vista para el login utilizando LoginView de Django
class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'