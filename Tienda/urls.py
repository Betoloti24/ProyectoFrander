from rest_framework import routers
from django.urls import path, include
from Tienda.controllers import UsuarioController, RopaController, CarritoController

urlpatterns = [
    path('usuarios/', UsuarioController.usuario_list),
    path('usuarios/<int:pk>/', UsuarioController.usuario_detail),
    path('usuarios/inicio_sesion/', UsuarioController.inicio_sesion),
    path('usuarios/cambiar_clave/', UsuarioController.cambio_clave),
    path('ropas/', RopaController.ropa_list),
    path('ropas/<int:pk>/', RopaController.ropa_detail),
    path('carritos/', CarritoController.agregar_al_carrito),
    path('carritos/<int:id_usuario>/<int:id_ropa>', CarritoController.eliminar_del_carrito),
    path('carritos/<int:id_usuario>', CarritoController.detalle_carrito),
]