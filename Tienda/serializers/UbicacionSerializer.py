from rest_framework import serializers
from Tienda.models import Ubicacion

class UbicacionSerial(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['id', 'nombre', 'tipo', 'id_padre']