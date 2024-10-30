# web/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='equipos')
    imagen = models.URLField(blank=True, null=True)  # Asumimos una URL para la imagen
    estado = models.CharField(max_length=45, choices=[('disponible', 'Disponible'), ('arrendado', 'Arrendado'), ('mantenimiento', 'Mantenimiento')])

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arriendos')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='arriendos')
    fecha = models.DateField()
    observacion = models.TextField(blank=True, null=True)
    danado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.equipo.nombre} - {self.fecha}"
    
@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    if sender.name == 'web':  # Asegurarse de que solo se ejecute en la app 'web'
        Group.objects.get_or_create(name='Cliente')
        Group.objects.get_or_create(name='Operario')