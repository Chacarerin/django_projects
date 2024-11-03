from django.contrib import admin
from .models import Categoria, TipoLibro, Libro, Prestamo
from .models import UserProfile
from django.contrib.auth.models import User

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(TipoLibro)
class TipoLibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'dias_prestamo', 'multa_dia_atraso')
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'tipo', 'disponible')
    search_fields = ('titulo', 'autor')
    list_filter = ('categoria', 'tipo', 'disponible')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion_esperada', 'fecha_devolucion_real', 'multa_total', 'activo')
    search_fields = ('usuario__username', 'libro__titulo')
    list_filter = ('activo',)

# Para extender la visualización del usuario en el panel admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# Extender el modelo User para incluir el perfil de usuario
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'staff_status', 'tipo_usuario')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    inlines = [UserProfileInline]

    def staff_status(self, obj):
        return obj.is_staff
    staff_status.short_description = 'Staff Status'
    staff_status.boolean = True

    def tipo_usuario(self, obj):
        return obj.userprofile.tipo
    tipo_usuario.short_description = 'Tipo de Usuario'

# Desregistrar el User model predeterminado y registrarlo con la configuración personalizada
admin.site.unregister(User)
admin.site.register(User, UserAdmin)