from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tienda.models import Factura
from Tienda.serializers.FacturaSerializer import FacturaSerializer

@api_view(['GET'])
def facturas_list(request, pk):
    facturas = Factura.objects.filter(id_usuario = pk)
    serializer = FacturaSerializer(facturas, many=True)
    return Response({'error': False, 'mensaje': 'Listado de facturas', 'data': serializer.data}, status=status.HTTP_200_OK)