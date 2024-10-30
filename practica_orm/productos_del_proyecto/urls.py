from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/username/<str:cadena>/', views.mostrar_username, name='mostrar_username'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('crearusuario/', views.registro, name='registro'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]