from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroUsuarioForm

def index(request):
    imagen_path = 'piezasRevive/images/fondo.jpg'

    return render(request, 'piezasRevive/index.html', {'imagen_path': imagen_path})

def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'piezasRevive/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Cambia 'home' al nombre de tu vista de inicio
    else:
        form = AuthenticationForm()
    return render(request, 'piezasRevive/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Cambia 'login' al nombre de tu vista de inicio de sesión
