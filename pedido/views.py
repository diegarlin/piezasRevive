from django.shortcuts import render
from .models import Pedido, ItemPedido
from carrito.carrito import Carrito
from producto.models import Producto
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
#from pagos.views import success

# Create your views here.

def procesar_pedido(request):
    request.session['telefono'] = request.POST['telefono']
    request.session['direccion'] = request.POST['direccion']
    request.session['nombre'] = request.POST['nombre']
    request.session['apellido'] = request.POST['apellido']
    request.session['email'] = request.POST['email']
    request.session['forma_pago'] = request.POST['formaPago']
    request.session['forma_entrega'] = request.POST['formaEntrega']
    
    
    
    if (request.POST['formaPago'] == 'tarjeta'):
        #messages.error(request, "El proceso de pago con tarjeta está en desarrollo") 
        return redirect("/pagos")
    else:
        #success(request)
        return redirect("/")


def hacer_pedido(request):
    pedido=Pedido()
    if request.user.is_authenticated:
        pedido.nombre_cliente = request.user.first_name
        pedido.apellido_cliente = request.user.last_name
        pedido.email = request.user.email
    else:
        pedido.nombre_cliente = ""
        pedido.apellido_cliente = ""
        pedido.email = ""
    return render(request,'form.html', {'pedido':pedido})

def buscar_pedido(request):
    return render(request, 'search.html', request)



@csrf_exempt
def mostrar_pedido(request):
   
    if ('pedido_id' in request.POST):
        if not Pedido.objects.filter(id=request.POST['pedido_id']).exists():
            messages.error(request, "No existe pedido con dicho identificador. Pruebe de nuevo")
            return redirect("/pedidos/buscarPedido")
        pedido = Pedido.objects.get(id=request.POST['pedido_id'])
        request.session['old_pedido_id'] = request.POST['pedido_id']
    else:
        if not Pedido.objects.filter(id=request.session['old_pedido_id']).exists():
            messages.error(request, "No existe pedido con dicho identificador. Pruebe de nuevo")
            return redirect("/pedidos/buscarPedido")
        pedido = Pedido.objects.get(id=request.session['old_pedido_id'])

    itemspedido = ItemPedido.objects.filter(pedido=pedido.pk)
    total = sum([linea.producto.precio * linea.cantidad for linea in itemspedido])
    context = {"lineas_pedido": itemspedido, "pedido":pedido, "total":total, "index":0}
    return render(request, 'show.html', context)

