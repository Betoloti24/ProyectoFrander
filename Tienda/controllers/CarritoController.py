from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tienda.models import Carrito, Ropa, Usuario
from Tienda.serializers.CarritoSerializer import CarritoSerializer

# agregar
@api_view(['POST'])
def agregar_al_carrito(request):
    # extraemos los datos del cuerpo
    data = request.data
    cantidad = data.get("cantidad", None)
    id_usuario = data.get("id_usuario", None)
    id_ropa = data.get("id_ropa", None)

    # Verificamos los valores
    if not id_usuario or not id_ropa or not cantidad:
        return Response({'error': True, 'mensaje': 'No se han enviado todos los datos', 'data': []}, status=status.HTTP_400_BAD_REQUEST)

    # buscamos la prenda de ropa
    try:
        producto = Ropa.objects.get(id=id_ropa)
    except Ropa.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha conseguido la prenda de ropa', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
    # buscamos al usuario
    try:
        usuario = Usuario.objects.get(cedula=id_usuario)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado al usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
    # verificamos si ese producto ya no esta en el carrito del usuario
    try:
        prenda_en_carrito = Carrito.objects.get(id_usuario=id_usuario, id_ropa=id_ropa, id_factura=None)
        # creamos un nuevo registro en el carrito
        return Response({'error': True, 'mensaje': 'La prenda ya está agregada al carrito del usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    except Carrito.DoesNotExist:
        serializer = CarritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error': False, 'mensaje': 'Prenda de ropa agregada al carrito con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else: 
            return Response({'error': True, 'mensaje': 'No se pudo agregar la prenda al carrito', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# eliminar 
@api_view(['DELETE'])
def eliminar_del_carrito(request, id_usuario, id_ropa):
    # buscamos al usuario
    try:
        usuario = Usuario.objects.get(cedula=id_usuario)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado al usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
    # buscamos la prenda de ropa
    try:
        producto = Ropa.objects.get(id=id_ropa)
    except Ropa.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha conseguido la prenda de ropa', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
    # verificamos si ese producto ya no esta en el carrito del usuario
    try:
        prenda_en_carrito = Carrito.objects.get(id_usuario=id_usuario, id_ropa=id_ropa, id_factura=None)
        prenda_en_carrito.delete()
        return Response({'error': False, 'mensaje': 'Prenda de ropa eliminada del carrito con exito', 'data': []}, status=status.HTTP_200_OK)
    except Carrito.DoesNotExist:
        return Response({'error': True, 'mensaje': 'La prenda no está agregada al carrito del usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
# listar y actualizar
@api_view(['GET', 'PUT'])
def detalle_carrito(request, id_usuario):
    # buscamos al usuario
    try:
        usuario = Usuario.objects.get(cedula=id_usuario)
    except Usuario.DoesNotExist:
        return Response({'error': True, 'mensaje': 'No se ha encontrado al usuario', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
    
    # listado
    if request.method == 'GET':
        carrito = Carrito.objects.filter(id_usuario=id_usuario, id_factura=None)
        serializer = CarritoSerializer(carrito, many=True)
        return Response({'error': False, 'mensaje': 'Listado del carrito del usuario', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    # actualizar existencia
    elif request.method == 'PUT':
        # extraemos los datos del cuerpo
        cantidad = request.data.get("cantidad", None)
        prenda = request.data.get("id_ropa", None)
        if not prenda or not cantidad:
            return Response({'error': True, 'mensaje': 'No se han incluido todos los datos', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
        
        # buscamos la prenda de ropa
        try:
            producto = Ropa.objects.get(id=prenda)
        except Ropa.DoesNotExist:
            return Response({'error': True, 'mensaje': 'No se ha conseguido la prenda de ropa', 'data': []}, status=status.HTTP_400_BAD_REQUEST)

        # actualizamos la existencia
        carrito = Carrito.objects.filter(id_usuario=id_usuario, id_ropa=prenda, id_factura=None).first()
        if carrito:
            carrito.cantidad = cantidad
            carrito.save()
            return Response({'error': False, 'mensaje': 'Existencia del carrito actualizado con exito', 'data':[]}, status=status.HTTP_200_OK)
        else:
            return Response({'error': True, 'mensaje': 'No se ha encontrado la prenda en el carrito', 'data': []}, status=status.HTTP_400_BAD_REQUEST)
