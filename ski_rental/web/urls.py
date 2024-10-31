from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('register/', views.registro, name='register'), 
    path('equipos/<int:equipo_id>/arrendar/', views.arrendar_equipo, name='arrendar_equipo'),
    path('arriendos/', views.lista_arriendos, name='lista_arriendos'),  # Ruta para operarios
    path('arriendos/<int:arriendo_id>/observacion/', views.agregar_observacion, name='agregar_observacion'),
    path('arriendos/<int:arriendo_id>/danado/', views.marcar_danado, name='marcar_danado'),
]