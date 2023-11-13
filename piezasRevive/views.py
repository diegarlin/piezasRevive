from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    imagen_path = 'piezasRevive/images/fondo.jpg'

    return render(request, 'piezasRevive/index.html', {'imagen_path': imagen_path})