from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Tienda.models import Categoria
from Tienda.serializers.CategoriaSerializer import CategoriaSerializer

@api_view(['GET'])
def categoria_list(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    data = {
        "error": False,
        "mensaje": 'Lista de categorias',
        "data": serializer.data
    }
    return Response(data)