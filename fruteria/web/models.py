# web/models.py
from django.db import models
from django.contrib.auth.models import User

# Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    unidades = models.PositiveSmallIntegerField()
    precio_por_unidad = models.IntegerField()

    def __str__(self):
        return self.nombre

# Modelo de Formato
class Formato(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=45)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"

# Modelo de Venta
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id} - {self.usuario.username} - {self.fecha}"

# Modelo Contiene para representar la relación muchos-a-muchos entre Venta y Producto
class Contiene(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.venta} contiene {self.producto}"
    
# Creación de usarios usando choices:

class UserProfile(models.Model):
    TIPOS_USUARIO = (
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador')
    )
    tipo = models.CharField(max_length=50, choices=TIPOS_USUARIO, default='cliente')
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        id = self.user.id
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.username
        tipo = self.tipo
        return f'{id} | {nombre} {apellido} | {usuario} | {tipo}'