from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('formacion/', views.academic, name='academic'),
    path('experiencia/', views.work, name='work'),
]