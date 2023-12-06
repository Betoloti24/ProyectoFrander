from django.db.models import Q
from .models import Ropa, Usuario

# filtrar prendas por preferencias de usuario
def preferencias_de_usuario(id_usuario):
    usuario = Usuario.objects.get(cedula = id_usuario)
    preferencias = [categoria['nombre'] for categoria in usuario.preferencias.values()]
    prendas_recomendadas = Ropa.objects.filter(categorias__nombre__in=preferencias).filter(Q(genero=usuario.genero) | Q(genero='Unisex')).distinct()
    return prendas_recomendadas

# filtrar prendas por preferencias de otros usuarios con los mismos gustos que el usuario principal
def preferencias_de_otros_usuarios(id_usuario):
    # preferencias del usuario actual
    usuario = Usuario.objects.get(cedula = id_usuario)
    preferencias_usuario = [categoria['nombre'] for categoria in usuario.preferencias.values()]
    preferencias = set(preferencias_usuario)
    # obtener todos los usuarios que tienen las mismas preferencias del usuario actual
    usuarios_con_mismas_preferencias = Usuario.objects.filter(preferencias__nombre__in=preferencias_usuario).filter(~Q(cedula=id_usuario)).distinct()
    # guardamos las nuevas preferencias
    otras_preferencias = set()
    for us in usuarios_con_mismas_preferencias:
        preferencias_otro_usuario = set([categoria['nombre'] for categoria in us.preferencias.values()])
        otras_preferencias = otras_preferencias.union(preferencias_otro_usuario)
    # prendas con las preferencias de otros usuarios, diferentes al del usuario actual
    preferencias_recomendadas = list(otras_preferencias - preferencias)
    prendas_recomendadas = Ropa.objects.filter(categorias__nombre__in=preferencias_recomendadas).filter(Q(genero=usuario.genero) | Q(genero='Unisex')).distinct()
    return prendas_recomendadas

# filtrar por prendas mas vendidas
def prendas_mas_vendidas():
    
    return Ropa.objects.all()