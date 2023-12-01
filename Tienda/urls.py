from rest_framework import routers
from django.urls import path, include
from Tienda.controllers import UsuarioController, RopaController

urlpatterns = [
    path('usuarios/', UsuarioController.usuario_list),
    path('usuarios/<int:pk>/', UsuarioController.usuario_detail),
    path('usuarios/correo/', UsuarioController.usuario_detail_correo),
    path('ropas/', RopaController.ropa_list),
    path('ropas/<int:pk>/', RopaController.ropa_detail),
]