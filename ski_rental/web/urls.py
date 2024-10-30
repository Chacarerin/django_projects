# web/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('equipos/<int:equipo_id>/arrendar/', views.arrendar_equipo, name='arrendar_equipo'),
    path('arriendos/', views.listar_arriendos, name='listar_arriendos'),
]