from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroUsuarioForm, CorreoElectronicoAuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request):
    return render(request, 'piezasRevive/index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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
        form = CorreoElectronicoAuthenticationForm()

    return render(request, 'piezasRevive/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
