from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = HTMLField()  # TinyMCE para contenido enriquecido
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    vistas = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.nombre} en {self.post}'