from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('laboratorios/', views.lista_laboratorios, name='lista_laboratorios'),
    path('laboratorios/agregar/', views.agregar_laboratorio, name='agregar_laboratorio'),
    path('laboratorios/editar/<int:id>/', views.editar_laboratorio, name='editar_laboratorio'),  
    path('laboratorios/eliminar/<int:id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),  
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]