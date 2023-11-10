from django.db import models

class MetodoPago(models.TextChoices):
    EFECTIVO = 'efectivo', 'Efectivo'
    TARJETA = 'tarjeta', 'Tarjeta'
    PAGO_MOVIL = 'pago_movil', 'Pago Móvil'