from rest_framework import serializers
from Tienda.models import Ropa

class RopaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ropa
        fields = ['id', 'nombre', 'precio_venta', 'marca', 'genero', 'categorias', 'imagen']