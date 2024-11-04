from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Producto, Venta, CompraStock

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'perfil de usuario'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'get_tipo')
    list_filter = ('is_staff', 'userprofile__tipo')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    def get_tipo(self, instance):
        return instance.userprofile.tipo
    get_tipo.short_description = 'Tipo de Usuario'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'formato_compra', 'cantidad_por_formato', 
                   'unidad_medida', 'stock_actual', 'precio_venta', 
                   'ultima_actualizacion')
    list_filter = ('unidad_medida',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'usuario', 'cantidad_vendida', 'precio_unitario', 
                   'total', 'fecha_venta', 'unidad_medida')
    list_filter = ('producto', 'fecha_venta', 'unidad_medida', 'usuario')
    search_fields = ('producto__nombre', 'usuario__username')
    ordering = ('-fecha_venta',)
    readonly_fields = ('total',)

@admin.register(CompraStock)
class CompraStockAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad_formatos', 'total_agregado', 
                   'fecha_compra', 'unidad_medida')
    list_filter = ('producto', 'fecha_compra', 'unidad_medida')
    search_fields = ('producto__nombre',)
    ordering = ('-fecha_compra',)