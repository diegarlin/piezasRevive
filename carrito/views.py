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

    messages.success(request, "Añadido exitosamente")
    carrito.agregar(producto=producto)
    
    return redirect(request.GET['next'])


def eliminar_producto(request, producto_id):

    carrito=Carrito(request)

    producto=Producto.objects.get(id=producto_id)

    messages.info(request, "Borrado exitosamente")
    carrito.eliminar(producto=producto)

    return redirect(request.GET['next'])


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    if not (str(producto_id) in carrito.carrito):
        messages.error(request, f"No puedes eliminar {producto.nombre} ya que no está en tu carrito.")
    elif int(request.GET.get('cantidad', 0)) <= carrito.carrito[str(producto_id)]["cantidad"]:
        carrito.restar(producto=producto)
        messages.info(request, "Borrado exitosamente")
    else:
        messages.error(request, f"No puedes eliminar más {producto.nombre} de los que tienes en tu carrito.")

    return redirect(request.GET.get('next', '/'))

    

def limpiar_carrito(request):

    carrito=Carrito(request)

    messages.info(request, "Carrito limpiado")
    carrito.limpiar_carrito()

    return redirect('../carrito/')

def ver_carrito(request):
    carrito = Carrito(request)
    
    return render(request, 'carrito.html', {'carrito': carrito})



