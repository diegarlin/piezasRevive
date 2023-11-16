from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroUsuarioForm, CorreoElectronicoAuthenticationForm, EditarPerfilForm 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'piezasRevive/index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'piezasRevive/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CorreoElectronicoAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        if request.user.is_authenticated:
            return redirect('index')
        form = CorreoElectronicoAuthenticationForm()

    return render(request, 'piezasRevive/login.html', {'form': form})



@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, '¡Deslogeo exitoso!')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def editar_perfil(request):
    if not request.user.is_authenticated:
        messages.error(request, '¡Debe estar logeado!', extra_tags='timer_duration:3000') 
        return redirect('login')

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('index')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'piezasRevive/editar_perfil.html', {'form': form})
