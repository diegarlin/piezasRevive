# reclamaciones/models.py

from django.db import models
from piezasRevive.models import PerfilUsuario
from pedido.models import Pedido

class Reclamacion(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    motivo = models.TextField()