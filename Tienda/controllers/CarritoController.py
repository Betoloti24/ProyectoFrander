


# carrito
@api_view(['POST', 'DELETE', 'PUT'])
def gestionar_carrito(requiest, pk):
    # buscamos la prenda de roa
    try:
        producto = Ropa.objects.get(id=pk)
    except Ropa.DoesNotExist:
        return Response({"error": "No se encontro el producto"}, status=status.HTTP_400_BAD_REQUEST)
    
    # agregamos
    if requiest.method == 'POST':