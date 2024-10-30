from django.db import models
from django.core.exceptions import ValidationError

def validar_anno(value):
    if value < 2015:
        raise ValidationError("El año de fabricación no puede ser anterior a 2015")

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, default="")  
    pais = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.IntegerField(validators=[validar_anno])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.f_fabricacion < 2015:
            raise ValidationError("El año de fabricación no puede ser anterior a 2015")