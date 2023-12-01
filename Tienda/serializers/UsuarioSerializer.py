from rest_framework import serializers
from Tienda.models import Usuario

# consulta
class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'apellido', 'f_nacimiento', 'genero', 'telefono', 'correo', 'id_pais', 'preferencias']