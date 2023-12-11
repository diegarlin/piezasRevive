# reclamaciones/models.py

from django.db import models
from piezasRevive.models import PerfilUsuario
from pedido.models import Pedido
from django.contrib.auth.models import User

class Reclamacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    descripcion = models.TextField(default=" ")