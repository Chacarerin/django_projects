from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

# Perfil de Usuario usando choices para el tipo de usuario
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

class Producto(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('KG', 'Kilogramos'),
        ('UNIDAD', 'Unidades')
    ]
    
    nombre = models.CharField(max_length=255)
    formato_compra = models.CharField(max_length=255, help_text="ej: Cajón/Saco")
    cantidad_por_formato = models.FloatField(help_text="17kg/10und")
    unidad_medida = models.CharField(
        max_length=10,
        choices=UNIDAD_MEDIDA_CHOICES,
        default='KG'
    )
    stock_actual = models.FloatField(help_text="en kg/und")
    precio_venta = models.FloatField(help_text="por kg/und")
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - Stock: {self.stock_actual} {self.unidad_medida}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

User = get_user_model()

class Venta(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('KG', 'Kilogramos'),
        ('UNIDAD', 'Unidades')
    ]

    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ventas'
    )  # Nuevo campo para registrar el usuario
    cantidad_vendida = models.FloatField(help_text="en kg/und")
    precio_unitario = models.FloatField()
    total = models.FloatField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
    unidad_medida = models.CharField(
        max_length=10,
        choices=UNIDAD_MEDIDA_CHOICES,
        default='KG'
    )

    def save(self, *args, **kwargs):
        if not self.total:
            self.total = self.cantidad_vendida * self.precio_unitario
        
        if self.producto:
            self.producto.stock_actual -= self.cantidad_vendida
            self.producto.save()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.producto.nombre if self.producto else 'Producto desconocido'} - {self.cantidad_vendida} {self.unidad_medida}"

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

class CompraStock(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('KG', 'Kilogramos'),
        ('UNIDAD', 'Unidades')
    ]
    
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE,
        null=True,  # Permitimos null temporalmente
        blank=True  # Permitimos que esté vacío en formularios
    )
    cantidad_formatos = models.IntegerField()
    total_agregado = models.FloatField(help_text="en kg/und")
    fecha_compra = models.DateTimeField(auto_now_add=True)
    unidad_medida = models.CharField(
        max_length=10,
        choices=UNIDAD_MEDIDA_CHOICES,
        default='KG'
    )

    def save(self, *args, **kwargs):
        if self.producto:  # Solo actualizamos stock si hay producto
            self.producto.stock_actual += self.total_agregado
            self.producto.save()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Compra de {self.producto.nombre if self.producto else 'Producto desconocido'} - {self.cantidad_formatos} formatos"

    class Meta:
        verbose_name = "Compra de Stock"
        verbose_name_plural = "Compras de Stock"