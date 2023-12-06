from django.db import models
import os 

# Create your models here.
"""
    Modelo de Ubicacion:
    *# id: numerico(10)
    * nombre: cadena(30)
    * tipo: cadena(10) (Check)
    * id_padre: numerico(10) (FK)
"""
class Ubicacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10, choices=[('País', 'País'), ('Ciudad', 'Ciudad')])
    id_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'

    def __str__(self):
        return f'{self.tipo}: {self.nombre}'
    
"""
    Modelo de Categoria:
    *# id: numerico(10)
    * nombre: cadena(20)
"""
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

"""
    Modelo de Usuario:
    *# cedula: numerico(10)
    * nombre: cadena(30)
    * apellido: cadena(30)
    * f_nacimiento: fecha(YYYY/MM/DD)
    * genero: cadena(10) (Check)
    * telefono: cadena(15)
    * correo: cadena(30)
    * id_pais: numerico(10) (FK)
"""
class Usuario(models.Model):
    cedula = models.PositiveBigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    f_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=30)
    id_ciudad = models.ForeignKey('Ubicacion', on_delete=models.SET_NULL, null=True, blank=True)
    preferencias = models.ManyToManyField('Categoria', blank=True)
    clave_acceso = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

"""
    Modelo de Ropa
    *# id: numerico(10)
    * nombre: cadena(30)
    * precio_venta: numerico(9,2)
    * marca: cadena(20)
    * genero: cadena(10) (Check) 
    * imagen: imagen()
"""
class Ropa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio_venta = models.DecimalField(max_digits=9, decimal_places=2)
    marca = models.CharField(max_length=20)
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Unisex', 'Unisex')])
    categorias = models.ManyToManyField('Categoria') 
    imagen = models.ImageField(upload_to='ropa/', null=True, blank=True)
    class Meta:
        verbose_name = 'Ropa'
        verbose_name_plural = 'Ropas'

    def delete(self, *args, **kwargs):
        # Eliminar la imagen del producto del sistema de archivos
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nombre

"""
    Modelo de Factura
    *# id: numerico(10)
    * f_facturacion: fecha(YYYY/MM/DD)
    * monto_total: numerico(9,2)
    * id_usuario: numerico(10) (FK)
"""
class Factura(models.Model):
    id = models.BigAutoField(primary_key=True)
    f_facturacion = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=9, decimal_places=2)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f'{self.id}'
    
"""
    Modelo de Carrito
    * cantidad: numerico(2) (FK)
    * id_usuario: numerico(10) (FK)
    * id_ropa: numerico(10) (FK)
    º id_factura: numerico(10) (FK)
"""
class Carrito(models.Model):
    cantidad = models.PositiveSmallIntegerField()
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_ropa = models.ForeignKey('Ropa', on_delete=models.CASCADE)
    id_factura = models.ForeignKey('Factura', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        return f'{self.id_usuario} - {self.id_ropa} - {self.cantidad}'