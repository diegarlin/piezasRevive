from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from producto.models import Producto
from .models import ItemCarrito

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, creado = ItemCarrito.objects.get_or_create(producto=producto)
    carrito_item.cantidad += 1
    carrito_item.save()
    return render(request, 'agregar_al_carrito.html', {'producto': producto})

def ver_carrito(request):
    carrito = ItemCarrito.objects.all()

    for item in carrito:
        item.subtotal = item.producto.precio * item.cantidad

    total = sum(item.producto.precio * item.cantidad for item in carrito)
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})
