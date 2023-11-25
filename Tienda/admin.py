from django.contrib import admin
from .models import Ubicacion, Categoria, Usuario, Ropa, Factura, Carrito

# Creamos los registros de las tablas en el administrador por el patron de decorador
@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'id_padre')
    list_filter = ('tipo', 'id_padre')
    search_fields = ('nombre', )

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre_completo', 'f_nacimiento', 'genero', 'telefono')
    list_filter = ('genero', 'id_pais',)
    date_hierarchy = 'f_nacimiento'
    search_fields = ('nombre', 'apellido',)

    def nombre_completo(self, obj):
        return f'{obj.nombre} {obj.apellido}'

@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio_venta', 'genero', 'tipo')
    list_filter = ('genero','tipo')
    search_fields = ('nombre',)

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_facturacion', 'id_usuario', 'monto_total')
    list_filter = ('id_usuario',)
    date_hierarchy = 'f_facturacion'

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_ropa', 'cantidad', 'id_factura')
    list_filter = ('id_usuario', 'id_ropa')
    search_fields = ('id_usuario', 'id_ropa')