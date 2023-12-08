from rest_framework import routers
from django.urls import path, include
from Tienda.controllers import UsuarioController, RopaController, CarritoController, CategoriaController

urlpatterns = [
    path('usuarios/', UsuarioController.consultar_usuarios),
    path('usuarios/<int:pk>/', UsuarioController.usuario_detail),
    path('usuarios/registro/', UsuarioController.registro_usuario),
    path('usuarios/inicio_sesion/', UsuarioController.inicio_sesion),
    path('usuarios/cambiar_clave/', UsuarioController.cambio_clave),
    path('usuarios/cambiar_preferencias/<int:pk>/', UsuarioController.cambiar_preferencias),
    
    path('ropas/', RopaController.ropa_list),
    path('ropas/<int:pk>/', RopaController.ropa_detail),
    
    path('carritos/', CarritoController.agregar_al_carrito),
    path('carritos/<int:id_usuario>/<int:id_ropa>/', CarritoController.eliminar_del_carrito),
    path('carritos/<int:id_usuario>/', CarritoController.detalle_carrito),
    path('carritos/pagar/<int:id_usuario>/', CarritoController.pagar_carrito),

    path('recomendaciones/preferencias_usuario/<int:pk>/', RopaController.recomendar_prendas_preferencias),
    path('recomendaciones/preferencias_otros_usuario/<int:pk>/', RopaController.recomendar_prendas_preferencias_otros_usuarios),
    path('recomendaciones/prendas_mas_vendidas/', RopaController.recomendar_prendas_mas_vendidas),

    path('categorias/', CategoriaController.categoria_list),
]