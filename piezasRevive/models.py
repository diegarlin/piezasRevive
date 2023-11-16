# usuarios/models.py

from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega aquí campos adicionales relacionados con el perfil del usuario si es necesario

    def __str__(self):
        return self.usuario.username