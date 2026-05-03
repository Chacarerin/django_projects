from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Modificamos el UserAdmin para incluir la nueva propiedad user_role
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_role')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

# Registramos User con la clase CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Registro de UserProfile para poder gestionarlo desde el admin si se desea
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name')