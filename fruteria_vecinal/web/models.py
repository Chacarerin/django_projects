from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    ROLES = (
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    )
    tipo = models.CharField(max_length=50, choices=ROLES, default='cliente')
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} | {self.tipo}'

# Agrega una propiedad al modelo User para acceder al tipo
@property
def user_role(self):
    return self.userprofile.tipo if hasattr(self, 'userprofile') else 'Sin perfil'

User.add_to_class("user_role", user_role)  # Agrega la propiedad al modelo User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Crea el perfil solo si el usuario fue recién creado
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Guarda el perfil si ya existe, para mantenerlo actualizado
        instance.userprofile.save()