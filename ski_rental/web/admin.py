# web/admin.py
from django.contrib import admin
from .models import Categoria, Equipo, Arriendo

# Registro de modelos
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Muestra estos campos en la lista
    search_fields = ('nombre',)      # Agrega una barra de búsqueda por nombre

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'estado')
    list_filter = ('categoria', 'estado')  # Agrega un filtro por categoría y estado
    search_fields = ('nombre',)            # Agrega una barra de búsqueda por nombre

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'equipo', 'fecha', 'danado')
    list_filter = ('fecha', 'danado')      # Filtro por fecha y estado de daño
    search_fields = ('user__username', 'equipo__nombre')  # Búsqueda por usuario y equipo
    date_hierarchy = 'fecha'               # Añade una jerarquía de fechas