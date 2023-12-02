# usuarios/models.py

from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    EXPRESS = 'express'
    NORMAL = 'normal'
    
    FORMA_ENTREGA = (
        (EXPRESS, 'express'),
        (NORMAL, 'normal'),     
    )

    forma_entrega = models.CharField(
        max_length=15,
        choices=FORMA_ENTREGA,
        default=NORMAL,
    )

    CONTRAREEMBOLSO = 'contrareembolso'
    TARJETA = 'tarjeta'

    FORMA_PAGO = (
        (CONTRAREEMBOLSO, 'contrareembolso'),
        (TARJETA, 'tarjeta'),     
    )

    forma_pago = models.CharField(
        max_length=15,
        choices=FORMA_PAGO,
        default=CONTRAREEMBOLSO,
    )

    domicilio = models.CharField(max_length=300, default="Avenida Reina Mercedes S/N ETSII")
    def __str__(self):
        return self.usuario.username