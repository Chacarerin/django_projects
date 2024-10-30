from django.contrib import admin
from .models import Fabricante, Producto

# Registrar el modelo Fabricante
@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')  # Campos que se mostrarán en la lista

# Registrar el modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabricante')  # Campos que se mostrarán en la lista
    list_filter = ('fabricante',)  # Filtro para filtrar por fabricante