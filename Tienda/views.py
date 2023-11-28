from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Ubicacion, Usuario, Ropa, Factura, Carrito, Categoria
from .serializers import UbicacionSerializer, UsuarioSerializer, RopaSerializer, FacturaSerializer, CarritoSerializer, CategoriaSerializer

### UBICACION
#### GET
class UbicacionListView(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

### CATEGORIA   
#### GET
class CategoriaListView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

### USUARIO
#### GET
class UsuarioListView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

### ROPA   
#### GET
class RopaListView(viewsets.ModelViewSet):
    queryset = Ropa.objects.all()
    serializer_class = RopaSerializer

### FACTURA
#### GET
class FacturaListView(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

### CARRITO
#### GET
class CarritoListView(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer