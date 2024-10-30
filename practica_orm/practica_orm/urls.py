from django.contrib import admin
from django.urls import path, include  # Importamos include para incluir las URLs de la aplicación

urlpatterns = [
    path('admin/', admin.site.urls),            # URL para el panel de administración de Django
    path('', include('productos_del_proyecto.urls')),  # Incluimos las URLs de la aplicación productos_del_proyecto
]