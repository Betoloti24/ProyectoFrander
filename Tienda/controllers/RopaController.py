from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tienda.models import Ropa, Usuario
from Tienda.serializers.RopaSerializer import RopaSerializer
from Tienda.modelo_ia import preferencias_de_usuario, preferencias_de_otros_usuarios, prendas_mas_vendidas

# creacion y listado
@api_view(['GET', 'POST'])
def ropa_list(request):
    # listado
    if request.method == 'GET':
        prenda = Ropa.objects.all()
        serializer = RopaSerializer(prenda, many=True)
        return Response({'error': False, 'mensaje': 'Listado de prendas de ropa', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    # creacion
    elif request.method == 'POST':
        serializer = RopaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': False, 'mensaje': 'Prenda de ropa creada con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else: 
            return Response({'error': True, 'mensaje': 'No se pudo crear la prenda de ropa', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# detalle, actualizacion y eliminacion
@api_view(['GET', 'PUT', 'DELETE'])
def ropa_detail(request, pk):
    # recuperamos la instancia de la prenda
    try:
        prenda = Ropa.objects.get(id=pk)
    except Ropa.DoesNotExist:
        return Response({'error': True, 'mensaje': 'La prenda de ropa no existe', 'data': []}, status=status.HTTP_404_NOT_FOUND)
    # actualizacion
    if request.method == 'PUT':
        serializer = RopaSerializer(prenda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': False, 'mensaje': 'Prenda de ropa actualizada con exito', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': True, 'mensaje': 'No se pudo actualizar la prenda de ropa', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # eliminacion
    elif request.method == 'DELETE':
        prenda.delete()
        return Response({'error': False, 'mensaje': 'Prenda de ropa eliminada con exito'}, status=status.HTTP_200_OK)

    # detalle
    elif request.method == 'GET':
        serializer = RopaSerializer(prenda)
        return Response({'error': False, 'mensaje': 'Detalle de la prenda', 'data': serializer.data}, status=status.HTTP_200_OK)

# recomendar por preferencias
@api_view(['GET'])
def recomendar_prendas_preferencias(request, pk):
    # recuperamos la instancia del usuario
    try:
        usuario = Usuario.objects.get(cedula=pk)
        preferencias = usuario.preferencias
        prendas = preferencias_de_usuario(pk)
        serializer = RopaSerializer(prendas, many=True)
        return Response({'error': False, 'mensaje': 'Listado de prendas de ropa recomendadas', 'data': serializer.data}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado al usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    except Ropa.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado prendas de ropa', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
# recomendar por preferencias de otros usuarios que tienen las mismas preferencias
@api_view(['GET'])
def recomendar_prendas_preferencias_otros_usuarios(request, pk):
    # recuperamos la instancia del usuario
    try:
        usuario = Usuario.objects.get(cedula=pk)
        preferencias = usuario.preferencias
        prendas = preferencias_de_otros_usuarios(pk)
        serializer = RopaSerializer(prendas, many=True)
        return Response({'error': False, 'mensaje': 'Listado de prendas de ropa recomendadas a partir de las preferencias de otros usuarios', 'data': serializer.data}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado al usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    except Ropa.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado prendas de ropa', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
# recomendar prendas mas vendidas
@api_view(['GET'])
def recomendar_prendas_mas_vendidas(request):
    # recuperamos la instancia del usuario
    try:
        prendas = prendas_mas_vendidas()
        serializer = RopaSerializer(prendas, many=True)
        return Response({'error': False, 'mensaje': 'Listado de prendas mas vendidas', 'data': serializer.data}, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado al usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    except Ropa.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado prendas de ropa', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    