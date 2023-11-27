from django.shortcuts import render, get_object_or_404, redirect
from .models import Reclamacion
from .forms import ReclamacionForm
from pedido.models import Pedido  # Add this line to import the Pedido model
from django.contrib.auth.models import User

# ... (other imports)

def crear_reclamacion(request, pedido_id):
    # Obtener el pedido asociado al ID
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if request.method == 'POST':
        # Si se envía un formulario, procesar los datos
        form = ReclamacionForm(request.POST)
        if form.is_valid():
            if pedido.usuario is None:
                # Si el usuario del pedido es None, usar el usuario admin
                usuario = User.objects.get(username='admin')
            else:
                # Si hay un usuario en el pedido, usar ese usuario
                usuario = pedido.usuario

            reclamacion = form.save(commit=False)
            reclamacion.usuario = usuario
            reclamacion.pedido = pedido
            reclamacion.save()
            return redirect('reclamaciones:detalle_reclamacion', reclamacion.id)
    else:
        # Si es una solicitud GET, mostrar el formulario vacío
        form = ReclamacionForm()

    return render(request, 'crear_reclamacion.html', {'form': form, 'pedido': pedido})


def detalle_reclamacion(request, reclamacion_id):
    reclamacion = get_object_or_404(Reclamacion, id=reclamacion_id)
    return render(request, 'detalle_reclamacion.html', {'reclamacion': reclamacion})
