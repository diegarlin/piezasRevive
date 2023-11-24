from django.db import models
from producto.models import Producto
from django.contrib.auth.models import User

class Pedido(models.Model):
    telefono=models.CharField(max_length=12)
    direccion=models.CharField(max_length=100)
    nombre_cliente=models.CharField(max_length=50)
    apellido_cliente=models.CharField(max_length=50)
    email=models.EmailField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    EN_ESPERA = 'en_espera'
    ENVIADO = 'enviado'
    ENTREGADO = 'entregado'
    
    ESTADO_PEDIDO = (
        (EN_ESPERA, 'en_espera'),
        (ENVIADO, 'enviado'),
        (ENTREGADO, 'entregado'),    
    )

    estado_pedido = models.CharField(
        max_length=10,
        choices=ESTADO_PEDIDO,
        default=EN_ESPERA,
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

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class ItemPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table='itemspedido'
        verbose_name='Item Pedido'
        verbose_name_plural='Items Pedidos'
        ordering=['id']