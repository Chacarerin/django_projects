from django.contrib import admin
from .models import UserProfile, Categoria, Equipo, Arriendo
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Clase para manejar la visualización y edición de UserProfile en el admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo')  # Mostrar el usuario y el tipo en la lista
    list_filter = ('tipo',)          # Permitir filtrar por tipo de usuario
    search_fields = ('user__username', 'user__email')  # Buscar por nombre de usuario y email

# Registrar UserProfile en el admin usando UserProfileAdmin
admin.site.register(UserProfile, UserProfileAdmin)

# Clase para extender el UserAdmin y mostrar el tipo de perfil
class CustomUserAdmin(UserAdmin):
    def userprofile_tipo(self, obj):
        return obj.userprofile.tipo
    userprofile_tipo.short_description = 'Tipo de Usuario'

    # Añadir el campo `userprofile_tipo` a la lista de visualización de usuarios
    list_display = UserAdmin.list_display + ('userprofile_tipo',)

# Reemplazar el UserAdmin predeterminado con el CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Registrar otros modelos
admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Arriendo)