from django.contrib import admin
from .models import Categoria, TipoLibro, Libro, Prestamo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(TipoLibro)
class TipoLibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'dias_prestamo', 'multa_dia_atraso')
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'tipo', 'disponible')
    search_fields = ('titulo', 'autor')
    list_filter = ('categoria', 'tipo', 'disponible')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion_esperada', 'fecha_devolucion_real', 'multa_total', 'activo')
    search_fields = ('usuario__username', 'libro__titulo')
    list_filter = ('activo',)