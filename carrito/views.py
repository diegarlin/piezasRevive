from django.shortcuts import render

from .carrito import Carrito

from producto.models import Producto

from django.shortcuts import redirect

from django.contrib import messages

# Create your views here.

def agregar_producto(request, producto_id):

    carrito=Carrito(request)

    producto=Producto.objects.get(id=producto_id)

    if (str(producto_id) in carrito.carrito):
        total = int(request.GET['cantidad']) + carrito.carrito[str(producto_id)]["cantidad"]
        if (total >  producto.stock):
            messages.error(request, f"No hay {total} copias disponibles, el stock de {producto.nombre} es {producto.stock} copias")
            return redirect(request.GET['next'])

    carrito.agregar(producto=producto)
    
    return redirect(request.GET['next'])


def eliminar_producto(request, producto_id):

    carrito=Carrito(request)

    producto=Producto.objects.get(id=producto_id)

    carrito.eliminar(producto=producto)

    return redirect(request.GET['next'])


def restar_producto(request, producto_id):

    carrito=Carrito(request)

    producto=Producto.objects.get(id=producto_id)

    carrito.restar(producto=producto)

    return redirect(request.GET['next'])


def limpiar_carrito(request):

    carrito=Carrito(request)

    carrito.limpiar_carrito()

    return redirect('../carrito/')

def ver_carrito(request):
    carrito = Carrito(request)
    
    return render(request, 'carrito.html', {'carrito': carrito})



