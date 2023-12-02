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
from pagos.views import success
from piezasRevive.models import PerfilUsuario

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
        return redirect("/pagos")
        
    else:
        return redirect("/pagos/success")


def hacer_pedido(request):
    pedido=Pedido()
    if request.user.is_authenticated:
        pedido_usuario = PerfilUsuario.objects.get(usuario= request.user)
        pedido.nombre_cliente = request.user.first_name
        pedido.apellido_cliente = request.user.last_name
        pedido.email = request.user.email
        pedido.forma_entrega = pedido_usuario.forma_entrega
        pedido.direccion = pedido_usuario.domicilio
        pedido.forma_pago = pedido_usuario.forma_pago
    else:
        pedido.nombre_cliente = ""
        pedido.apellido_cliente = ""
        pedido.email = ""
    return render(request,'form.html', {'pedido':pedido})

def buscar_pedido(request):
    return render(request, 'search.html')



@csrf_exempt
def mostrar_pedido(request):
   
    if ('pedido_id' in request.POST):
        if not Pedido.objects.filter(id=request.POST['pedido_id']).exists():
            messages.error(request, "No existe pedido con dicho identificador. Pruebe de nuevo")
            return redirect("/buscarPedido")
        pedido = Pedido.objects.get(id=request.POST['pedido_id'])
        request.session['old_pedido_id'] = request.POST['pedido_id']
    else:
        if not Pedido.objects.filter(id=request.session['old_pedido_id']).exists():
            messages.error(request, "No existe pedido con dicho identificador. Pruebe de nuevo")
            return redirect("/buscarPedido")
        pedido = Pedido.objects.get(id=request.session['old_pedido_id'])

    itemspedido = ItemPedido.objects.filter(pedido=pedido.pk)
    total = sum([linea.producto.precio * linea.cantidad for linea in itemspedido])
    total += pedido.gastos_envio
    context = {"lineas_pedido": itemspedido, "pedido":pedido, "total":total, "index":0, "pedido_id": request.session['old_pedido_id']}
    return render(request, 'show.html', context)

def mostrar_pedidos_usuario(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    itemspedido={}
    for pedido in pedidos:
        itemspedido[pedido] =ItemPedido.objects.filter(pedido=pedido.pk)
        pedido.precio_final = sum([linea.producto.precio * linea.cantidad for linea in itemspedido[pedido]])
        pedido.precio_final += pedido.gastos_envio
    context = {"lineas_pedido": itemspedido, "pedidos":pedidos}
    return render(request, 'pedidos.html',context)
