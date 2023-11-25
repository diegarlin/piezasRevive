from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Opinion
from .forms import OpinionForm
from producto.models import Producto
from piezasRevive.models import PerfilUsuario
from django.contrib.auth.models import User

@login_required
def crear_opinion(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.usuario = User.objects.get(username=request.user.username)  # Asociar el usuario autenticado
            opinion.producto = producto
            opinion.save()
            url = '/product/details/' + str(producto.id)
            return redirect(url)
    else:
        form = OpinionForm()

    return render(request, 'crear_opinion.html', {'form': form, 'producto': producto})
