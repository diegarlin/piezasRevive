# opiniones/models.py

from django.db import models
from piezasRevive.models import PerfilUsuario
from producto.models import Producto

class Opinion(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()
