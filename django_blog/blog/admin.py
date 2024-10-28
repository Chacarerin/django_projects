from django.contrib import admin
from .models import Post, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'vistas')
    list_filter = ('fecha_creacion', 'autor')
    search_fields = ('titulo', 'contenido')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'post', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('nombre', 'cuerpo')