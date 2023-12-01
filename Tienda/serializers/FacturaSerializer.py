from rest_framework import serializers
from Tienda.models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'f_facturacion', 'monto_total', 'id_usuario']
