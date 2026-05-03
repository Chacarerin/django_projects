from django.contrib import admin
from django.urls import path
from movies import views  # Importa las vistas de tu aplicación 'movies'

urlpatterns = [
    path('admin/', admin.site.urls),  # Solo debe haber un registro para 'admin'
    path('', views.movie_recommendation, name='movie_recommendation'),  # Tu vista principal
]