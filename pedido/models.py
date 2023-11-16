from django.db import models
from piezasRevive.models import PerfilUsuario
from producto.models import Producto

class Pedido(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemPedido')
    direccion_envio = models.TextField()
    metodo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, default='Pendiente')

class ItemPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)