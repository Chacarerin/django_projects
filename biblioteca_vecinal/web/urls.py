from django.urls import path
from . import views 

urlpatterns = [
    path('', views.book_list, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('arriendos/', views.mis_arriendos, name='mis_arriendos'),
    path('libros/<int:libro_id>/arrendar/', views.arrendar_libro, name='arrendar_libro'),
    path('libros/<int:libro_id>/retornar/', views.retornar_libro, name='retornar_libro'),
]
