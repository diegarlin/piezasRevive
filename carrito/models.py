from django.db import models
from piezasRevive.models import PerfilUsuario
from producto.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(PerfilUsuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
