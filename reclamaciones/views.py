from django.shortcuts import render, get_object_or_404, redirect
from .models import Reclamacion
from .forms import ReclamacionForm
from pedido.models import Pedido  
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect


def crear_reclamacion(request, pedido_id):
    
    pedido = get_object_or_404(Pedido, id=pedido_id)

   
    if (pedido.usuario == request.user):
        if request.method == 'POST':
        
            form = ReclamacionForm(request.POST)
            if form.is_valid():
                usuario = pedido.usuario if pedido.usuario else User.objects.get(username='admin')

                reclamacion = form.save(commit=False)
                reclamacion.usuario = usuario
                reclamacion.pedido = pedido
                reclamacion.save()
                return redirect('reclamaciones:detalle_reclamacion', reclamacion.id)
        else:
            
            form = ReclamacionForm()
    else:
        messages.info(request, 'No tienes permisos para acceder a esta vista. Inserte el correo con el que hizo este pedido')
        return redirect('reclamaciones:ingresar_correo', pedido_id=pedido.id)      

    return render(request, 'crear_reclamacion.html', {'form': form, 'pedido': pedido})



def detalle_reclamacion(request, reclamacion_id):
    reclamacion = get_object_or_404(Reclamacion, id=reclamacion_id)
    return render(request, 'detalle_reclamacion.html', {'reclamacion': reclamacion})

def ingresar_correo(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if request.method == 'POST':
        correo_ingresado = request.POST.get('correo', '')
        if correo_ingresado == pedido.email:
            return redirect('reclamaciones:crear_reclamacion_sinloguear', pedido_id=pedido.id)
        else:
            messages.error(request, 'El correo no es correcto.')
            return redirect("/")
    
    
    return render(request, 'ingresar_correo.html', {'pedido': pedido})


def crear_reclamacion_sinloguear(request, pedido_id):

    pedido = get_object_or_404(Pedido, id=pedido_id)

   
    if request.method == 'POST':

        form = ReclamacionForm(request.POST)
        if form.is_valid():
            reclamacion = form.save(commit=False)
            reclamacion.pedido = pedido
            reclamacion.save()
            return redirect('reclamaciones:detalle_reclamacion', reclamacion.id)
    else:

        form = ReclamacionForm()
        

    return render(request, 'crear_reclamacion.html', {'form': form, 'pedido': pedido})

def listar_reclamaciones_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    reclamaciones = Reclamacion.objects.filter(pedido=pedido)

    return render(request, 'listar_reclamaciones_pedido.html', {'pedido': pedido, 'reclamaciones': reclamaciones})
