from rest_framework import serializers
from .models import Ubicacion, Categoria, Usuario, Ropa, Factura, Carrito

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['id', 'nombre', 'tipo', 'id_padre']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'apellido', 'f_nacimiento', 'genero', 'telefono', 'correo', 'id_pais', 'preferencias']

class RopaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ropa
        fields = ['id', 'nombre', 'precio_venta', 'marca', 'genero', 'categorias', 'imagen']

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'f_facturacion', 'monto_total', 'id_usuario']

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['cantidad', 'id_usuario', 'id_ropa', 'id_factura']


