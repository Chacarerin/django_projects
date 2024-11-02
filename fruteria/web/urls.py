from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              
    path('login/', views.login_view, name='login'),  
    path('register/', views.register, name='register'), 
    path('logout/', views.logout_view, name='logout'),
    path('ventas/', views.ventas, name='ventas'),  # Vista para Ventas
    path('stock/', views.stock, name='stock'),
]