from django.urls import path
from . import views  # Importamos las vistas de la app 'movies'

urlpatterns = [
    path('', views.movie_recommendation, name='movie_recommendation'),  # Ruta para la vista de recomendación de películas
]