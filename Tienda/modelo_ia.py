from .models import Ropa, Usuario

# filtrar prendas por preferencias de usuario
def preferencias_de_usuario(id_usuario):

    return Ropa.objects.all()

# filtrar prendas por preferencias de otros usuarios con los mismos gustos que el usuario principal
def preferencias_de_otros_usuarios(id_usuario):

    return Ropa.objects.all()

# filtrar por prendas mas vendidas
def prendas_mas_vendidas():
    
    return Ropa.objects.all()