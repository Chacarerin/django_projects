from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Nombre: {self.nombre}'


class Equipo(models.Model):
    estados = (
        ('disponible', 'Disponible'),
        ('arrendado', 'Arrendado'),
        ('mantencion', 'Mantención')
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.URLField()
    precio = models.IntegerField()
    estado = models.CharField(max_length=45, default='disponible', choices=estados)
    categoria = models.ForeignKey(Categoria, related_name='equipos', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} | {self.nombre} | {self.estado} | {self.categoria.nombre} | {self.precio}'
        


class Arriendo(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    observacion = models.TextField(null=True, blank=True)
    danado = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='arriendos', on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, related_name='arriendos', on_delete=models.CASCADE)

    def __str__(self):
        id = self.id
        fecha = self.fecha
        observacion = self.observacion
        danado = self.danado
        usuario = self.user.username
        equipo = self.equipo.nombre
        categoria = self.equipo.categoria.nombre
        return f'{id} | Fecha: {fecha} | Obs: {observacion} | Está dañado?: {danado} | User: {usuario} | Eq: {equipo} | Cat: {categoria}'

class UserProfile(models.Model):
    tipos = (
        ('cliente', 'Cliente'),
        ('operario', 'Operario')
    )
    tipo = models.CharField(max_length=50, default='cliente', choices=tipos)
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    
    def __str__(self):
        id = self.user.id
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.username
        tipo = self.tipo
        return f'{id} | {nombre} {apellido} | {usuario} | {tipo}'