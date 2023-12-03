from django import forms
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from producto.models import Producto
from opinion.models import Opinion

Categorias = ('Interior',
    'Direccion',
    'Embrague',
    'Motor',
    'Freno',
    'Alumbrado',
    'Carroceria')

Marcas = ('Seat',
    'Audi',
    'Toyota',
    'Mini',
    'Honda',
    'Fiat')

# Create your views here.
# @login_required
def product(request):
    nombre_de_producto_buscado = request.GET.get("name")
    categoria_buscada = request.GET.get("categoria")
    marca_buscada = request.GET.get("marca")
    print(marca_buscada)

    lista_tuplas_productos = get_products_by_tuples(nombre_de_producto_buscado, categoria_buscada, marca_buscada)
    modelmap = {'tupla_producto':lista_tuplas_productos, 
                'categorias':Categorias,
                'marcas':Marcas}
    return render(request, 'producto/producto.html', modelmap)

def get_products_by_tuples(nombre_de_producto_buscado=None, categoria_buscada=None, marca_buscada=None):
    productos = []
    productos_todos = Producto.objects.all()
    for producto in productos_todos:
        categoria_valida = True
        marca_valida = True
        nombre_de_producto_buscado_valido = True

        if nombre_de_producto_buscado is not None:
            nombre_de_producto_buscado_valido = producto.nombre.lower().__contains__(nombre_de_producto_buscado.replace("+"," ").lower())
        if categoria_buscada is not None:
            print(categoria_buscada)
            categoria_valida = producto.categoria.lower() == categoria_buscada.lower()
        if marca_buscada is not None:
            print(marca_buscada)
            marca_valida = producto.marca.lower() == marca_buscada.lower()
        if categoria_valida and marca_valida and nombre_de_producto_buscado_valido:
            productos.append(producto)
            
    lista_tuplas_productos = []
    for i in range(0, len(productos), 2):
        lista_tuplas_productos.append(tuple(productos[i:i+2]))
    return lista_tuplas_productos


# @login_required
def detalles(request, product_id):
    producto = Producto.objects.get(id=product_id)
    opiniones_todas = Opinion.objects.all()
    opiniones=[]
    for opinion in opiniones_todas:
        if opinion.producto==producto:
            opiniones.append(opinion)
    
    return render(request, 'producto/productoDetalles.html', {'producto': producto, 'opiniones': opiniones})