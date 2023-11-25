from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.conf import settings
from carrito.carrito import Carrito
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pedido.models import Pedido, ItemPedido
from piezasRevive.models import PerfilUsuario
from producto.models import Producto
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


import json
import os
import stripe

def home(request):
    telefono = request.session['telefono']
    direccion = request.session['direccion']
    nombre = request.session['nombre']
    apellido = request.session['apellido']
    email = request.session['email']
    forma_pago = request.session['forma_pago']
    forma_entrega = request.session['forma_entrega']
    
    carrito=Carrito(request)
    
    lineas_pedido = list()
    for key, value in carrito.carrito.items():
        pieza = Producto.objects.get(pk=key)
        lineas_pedido.append(ItemPedido(
            producto=pieza,
            cantidad=value["cantidad"],
            pedido=None
        ))

    total = sum([linea.producto.precio * linea.cantidad for linea in lineas_pedido])
    
    request.session['total'] = total
    url = '/pagos/create-checkout-session/'
    context = {'url':url}
    return render(request,'pagar.html', context=context)

def success(request):
    
    telefono = request.session.get('telefono')
    direccion = request.session.get('direccion')
    nombre = request.session.get('nombre')
    apellido = request.session.get('apellido')
    email = request.session.get('email')
    forma_pago = request.session.get('forma_pago')
    forma_entrega = request.session.get('forma_entrega')
    
    carrito=Carrito(request)
    
    pedido = Pedido(telefono=telefono, direccion=direccion, nombre_cliente=nombre, apellido_cliente=apellido, email=email, forma_pago=forma_pago, estado_pedido = "en_espera", forma_entrega=forma_entrega)
    if request.user.is_authenticated:
        pedido.usuario = request.user #request.user
    pedido.save()

    lineas_pedido = list()
    for key, value in carrito.carrito.items():
        pieza = Producto.objects.get(pk=key)
        pieza.stock -= value["cantidad"]
        pieza.save()
        lineas_pedido.append(ItemPedido(
            producto=pieza,
            cantidad=value["cantidad"],
            pedido=pedido
        ))

    importe_total = sum([linea.producto.precio * linea.cantidad for linea in lineas_pedido])
    
    ItemPedido.objects.bulk_create(lineas_pedido)

    carrito.limpiar_carrito()
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre = nombre,
        emailusuario = email,
        direccion_entrega=direccion,
        importe_total=importe_total
        
    )

    #messages.success(request, f"El pedido se ha creado correctamente. Guarde el siguiente identificador para ver el estado de su pedido: {pedido.pk}")
    context = {'id':pedido.pk}
    return render(request,'success.html', context=context)

def enviar_mail(**kwargs):
    asunto="Gracias por realizar el pedido"
    mensaje=render_to_string("email.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre": kwargs.get("nombre"),
        "emailusuario": kwargs.get("emailusuario"),
        "direccion_entrega": kwargs.get("direccion_entrega"),
        "importe_total": kwargs.get("importe_total")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="gameprojectpgpi@gmail.com"
    to=kwargs.get("emailusuario")

    #send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

def cancel(request):
    return render(request,'cancel.html')
 
 
stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = settings.BASEURL

@csrf_exempt
def create_checkout_session(request):
    print("Entra en checkout")
   
    total = request.session.get('total')
    print(int(total))
      
    total_formated = str("%.2f" % total).replace('.','')
    
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
        'price_data': {
            'currency': 'eur',
            'product_data': {
                'name': 'Pago en GAME',
             },
             'unit_amount': total_formated,
         },
         'quantity': 1,
     }],
     mode='payment',
     success_url=YOUR_DOMAIN + '/pagos/success',
     cancel_url=YOUR_DOMAIN + '/pagos/cancel',
    )
    return JsonResponse({'id': session.id})
