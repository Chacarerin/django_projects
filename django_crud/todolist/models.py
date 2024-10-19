from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    completado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.titulo
    
    class Meta:
        # Agregar permisos personalizados en Meta
        permissions = [
            ('editor_access', 'Permiso para agregar, editar y eliminar tareas'),
        ]

class Visitas(models.Model):
    contador = models.IntegerField(default=0)

    def __str__(self):
        return f"Visitas: {self.contador}"