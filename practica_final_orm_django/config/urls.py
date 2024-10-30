from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laboratorio/', include('laboratorio.urls')),
    path('', include('laboratorio.urls')),
]
