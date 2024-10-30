from django.db import models

# Modelo Fabricante
class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del fabricante
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField()  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True, blank=True, default="")  # Relación con Fabricante
    f_vencimiento = models.DateField(null=True, blank=True)  # Asegúrate de que el campo esté definido así


    def __str__(self):
        return self.nombre