from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class TipoLibro(models.Model):
    nombre = models.CharField(max_length=50)
    dias_prestamo = models.IntegerField()
    multa_dia_atraso = models.IntegerField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="libros")
    tipo = models.ForeignKey(TipoLibro, on_delete=models.CASCADE, related_name="libros")
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prestamos")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="prestamos")
    fecha_prestamo = models.DateTimeField(default=timezone.now)
    fecha_devolucion_esperada = models.DateTimeField()
    fecha_devolucion_real = models.DateTimeField(blank=True, null=True)
    multa_total = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Calcula la fecha de devolución esperada
        if not self.fecha_devolucion_esperada:
            self.fecha_devolucion_esperada = self.fecha_prestamo + timedelta(days=self.libro.tipo.dias_prestamo)

        # Calcula la multa si hay atraso
        if self.fecha_devolucion_real:
            dias_atraso = (self.fecha_devolucion_real - self.fecha_devolucion_esperada).days
            if dias_atraso > 0:
                self.multa_total = dias_atraso * self.libro.tipo.multa_dia_atraso
            else:
                self.multa_total = 0

        # Cambia la disponibilidad del libro
        if self.fecha_devolucion_real:
            self.libro.disponible = True
            self.activo = False
        else:
            self.libro.disponible = False

        self.libro.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} por {self.usuario.username}"
    

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
        tipo = self.get_tipo_display()
        return f'{id} | {nombre} {apellido} | {usuario} | {tipo}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'userprofile'):
        UserProfile.objects.create(user=instance, tipo='cliente')