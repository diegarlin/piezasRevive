from django import forms
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



from producto.models import Producto

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
@login_required
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


@login_required
def detalles(request, product_id):
    producto = Producto.objects.get(id=product_id)
    form = {"producto":producto}
    
    return render(request, 'producto/productoDetalles.html', {'form': form})

@login_required
def nombre(request):
    return render(request, 'producto/nombre.html')


@login_required
@csrf_exempt
def search_by_name(request):
    if ('name' in request.POST):
        productos = Producto.objects.filter(nombre__icontains=request.POST['name'])
        request.session['old_nombre'] = request.POST['name']
    else:
        productos = Producto.objects.filter(nombre__icontains=request.session['old_nombre'])
    context = {"productos":productos, "index":0}
    return render(request, 'producto/producto.html')

'''
def genre(request):
    template = loader.get_template("genre.html")
    return HttpResponse(template.render(request=request))


def search_by_genre(request, genero):
    print(genero)
    template = loader.get_template("index.html")
    productos = producto.objects.filter(genero=genero)
    context = {"productos":productos, "index":0}
    return HttpResponse(template.render(context, request))
    

def console(request):
    template = loader.get_template("console.html")
    
    consolas = producto.objects.all().values("consola").distinct()
    context = {"consolas":consolas}
    return HttpResponse(template.render(context, request))

def search_by_console(request, consola):
    template = loader.get_template("index.html")
    productos = producto.objects.filter(consola=consola)
    context = {"productos":productos, "index":0}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login_django(request, user)
            setUserSession(user,request)
            messages.success(request, "Registro exitoso!!")
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form,})


@csrf_exempt
def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

@csrf_exempt
def post_logout(request):
    logout(request)
    request.session['logged'] = False
    request.session['username'] = 'Anonimo'
    return redirect("index")
@csrf_exempt
def post_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login_django(request, user)
        setUserSession(user,request)
        messages.success(request, "Inicio de sesión exitoso")
        return redirect("index")
    else:
        messages.error(request, "Error al iniciar sesión, intentelo de nuevo")
        template = loader.get_template("login.html")
        return HttpResponse(template.render(request = request))

def setUserSession(user,request):
     request.session['logged'] = True
     request.session['username']=user.get_username()


def politic(request):
        template = loader.get_template("politic.html")
        return HttpResponse(template.render(request = request))
'''