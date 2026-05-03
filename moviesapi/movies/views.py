import requests
import random
from django.shortcuts import render
from .forms import MovieSearchForm
from django.conf import settings

def get_random_words_from_text(text):
    """Dividir el texto en palabras y seleccionar algunas de forma aleatoria si el texto es largo"""
    words = text.split()
    # Si hay más de 5 palabras, seleccionamos aleatoriamente hasta 5 para la búsqueda
    if len(words) > 5:
        random_words = random.sample(words, 5)
        return ' '.join(random_words)
    return text  # Si tiene menos de 5 palabras, usamos todo el texto

def get_movies_by_description(query, exclude_ids):
    """Función para buscar películas usando la API de TMDb según la descripción (overview) y excluyendo películas ya vistas"""
    api_key = settings.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=es-ES"
    
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        # Filtrar las películas que contengan las palabras clave en la descripción (overview)
        # Excluir películas ya mostradas (basadas en exclude_ids)
        filtered_movies = [movie for movie in movies if query.lower() in movie['overview'].lower() and movie['id'] not in exclude_ids]
        return filtered_movies
    return []

def ensure_three_movies(movies, exclude_ids):
    """Función para asegurarse de que siempre tengamos 3 películas y excluir resultados previos"""
    api_key = settings.TMDB_API_KEY
    # Si ya tenemos 3 películas, no hacemos nada
    if len(movies) >= 3:
        return movies
    
    # Si no tenemos suficientes películas, obtenemos películas populares excluyendo las ya vistas
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=es-ES&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        popular_movies = response.json().get('results', [])
        # Excluir películas ya mostradas (basadas en exclude_ids)
        popular_movies = [movie for movie in popular_movies if movie['id'] not in exclude_ids]
        # Ordenar por puntuación de mayor a menor y completar hasta 3 resultados
        popular_movies = sorted(popular_movies, key=lambda x: x['vote_average'], reverse=True)
        while len(movies) < 3 and popular_movies:
            movies.append(popular_movies.pop(0))  # Agregar películas hasta tener 3
    return movies

def get_awarded_movies(exclude_ids):
    """Función para obtener películas premiadas de TMDb y excluir películas ya vistas"""
    api_key = settings.TMDB_API_KEY
    # Buscar películas ordenadas por puntuación y que hayan sido premiadas
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=es-ES&sort_by=vote_average.desc&vote_count.gte=500"
    
    response = requests.get(url)
    if response.status_code == 200:
        awarded_movies = response.json().get('results', [])
        # Excluir películas ya mostradas (basadas en exclude_ids)
        awarded_movies = [movie for movie in awarded_movies if movie['id'] not in exclude_ids]
        # Seleccionar aleatoriamente 3 películas premiadas
        return random.sample(awarded_movies, 3) if len(awarded_movies) >= 3 else awarded_movies
    return []

def movie_recommendation(request):
    form = MovieSearchForm()
    recommendations = []
    random_movies = []
    
    # Recuperar la lista de películas ya vistas de la sesión (usando 'exclude_ids')
    exclude_ids = request.session.get('exclude_ids', [])

    if request.method == 'POST':
        # Si el usuario hace clic en el botón "Buscar películas"
        if 'search_movies' in request.POST:
            form = MovieSearchForm(request.POST)
            if form.is_valid():
                # Obtener el texto del formulario y seleccionar palabras al azar si es muy largo
                mood = form.cleaned_data['mood']
                search_query = get_random_words_from_text(mood)
                # Buscar películas basadas en las palabras seleccionadas y la descripción
                recommendations = get_movies_by_description(search_query, exclude_ids)
                # Asegurarse de que siempre haya 3 películas en las recomendaciones
                recommendations = ensure_three_movies(recommendations, exclude_ids)
                
                # Guardar las IDs de las películas mostradas para evitar duplicados en la sesión
                exclude_ids += [movie['id'] for movie in recommendations]
                request.session['exclude_ids'] = exclude_ids
        
        # Si el usuario hace clic en el botón "Sorpréndeme"
        elif 'surprise_me' in request.POST:
            # Obtener películas premiadas sin requerir texto
            random_movies = get_awarded_movies(exclude_ids)
            
            # Guardar las IDs de las películas premiadas en la sesión
            exclude_ids += [movie['id'] for movie in random_movies]
            request.session['exclude_ids'] = exclude_ids

    return render(request, 'index.html', {
        'form': form,
        'recommendations': recommendations,
        'random_movies': random_movies
    })