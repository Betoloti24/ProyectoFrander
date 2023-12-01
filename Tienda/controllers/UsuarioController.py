from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tienda.models import Usuario
from Tienda.serializers.UsuarioSerializer import UserSerial

# creacion y listado de usuarios
@api_view(['GET', 'POST'])
def usuario_list(request):
    # listado
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UserSerial(usuarios, many=True)
        return Response({'error': False, 'mensaje': 'Listado de usuarios', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    # creacion
    elif request.method == 'POST':
        serializer = UserSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': False, 'mensaje': 'Usuario creado con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else: 
            return Response({'error': True, 'mensaje': 'No se pudo crear el usuario', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# actualizacion y eliminacion de usuarios
@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk):
    # recuperamos la instancia del usuario
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'El usuario no existe', 'data': []}, status=status.HTTP_404_NOT_FOUND)
    
    # actualizacion
    if request.method == 'PUT':
        serializer = UserSerial(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': False, 'mensaje': 'Usuario actualizado con exito', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': True, 'mensaje': 'No se pudo actualizar el usuario', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # eliminacion
    elif request.method == 'DELETE':
        usuario.delete()
        return Response({'error': False, 'mensaje': 'Usuario eliminado con exito'}, status=status.HTTP_200_OK)

    # detalle
    elif request.method == 'GET':
        serializer = UserSerial(usuario)
        return Response({'error': False, 'mensaje': 'Detalle de usuario', 'data': serializer.data}, status=status.HTTP_200_OK)
    
# detalle por correo
@api_view(['GET'])
def usuario_detail_correo(request):
    # recuperamos la instancia del usuario
    try:
        correo = request.data.get('correo', None)
        if correo:
            usuario = Usuario.objects.get(correo=correo)
        else:
            return Response({'error': True, 'mensaje': 'No se ha enviado el correo', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': True, 'mensaje': 'El usuario no existe', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
    # detalle
    if request.method == 'GET':
        serializer = UserSerial(usuario)
        return Response({'error': False, 'mensaje': 'Detalle de usuario', 'data': serializer.data}, status=status.HTTP_200_OK)