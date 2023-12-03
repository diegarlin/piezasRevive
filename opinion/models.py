# opiniones/models.py

from django.db import models
from piezasRevive.models import PerfilUsuario
from django.contrib.auth.models import User
from producto.models import Producto

class Opinion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f'{self.usuario} - {self.producto}'