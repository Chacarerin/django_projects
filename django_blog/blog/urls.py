from django.urls import path
from . import views
from .views import upload_image

urlpatterns = [
    path('', views.index, name='index'),  # Front page
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),  # Página de detalle del post
    path('upload-image/', upload_image, name='upload_image'),
]