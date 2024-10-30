from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Personalizar la vista de Laboratorio
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Mostrar ID y nombre
    ordering = ('id',)  # Ordenar por ID de forma ascendente

# Personalizar la vista de DirectorGeneral
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')  # Mostrar ID, nombre y el laboratorio relacionado
    ordering = ('id',)  # Ordenar por ID de forma ascendente

# Personalizar la vista de Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')  # Mostrar campos relevantes

    # Definir una función para mostrar solo el año en f_fabricacion
    #def mostrar_anio_fabricacion(self, obj):
        #return obj.f_fabricacion.year  # Devolver solo el año

    # Personalizar el encabezado de la columna en la lista
   # mostrar_anio_fabricacion.short_description = 'F Fabricación'

    ordering = ('id',)  # Ordenar los productos por ID

# Registrar los modelos con sus configuraciones personalizadas
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)