from rest_framework import serializers
from Tienda.models import Carrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['cantidad', 'id_usuario', 'id_ropa', 'id_factura']