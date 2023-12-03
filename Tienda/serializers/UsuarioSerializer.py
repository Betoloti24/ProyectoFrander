from rest_framework import serializers
from Tienda.models import Usuario

# consulta y creacion
class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'apellido', 'f_nacimiento', 'genero', 'telefono', 'correo', 'id_ciudad', 'preferencias', 'clave_acceso']

# cambiar clave
class UserSerialClave(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['correo','clave_acceso']

# actualizar
class UserSerialActualizar(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'apellido', 'f_nacimiento', 'genero', 'telefono', 'correo', 'id_ciudad', 'preferencias']