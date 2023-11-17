from django import forms
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from producto.models import Producto

# Create your views here.
@login_required
def product(request):
    productos = Producto.objects.all()
    form = {"productos":productos, "index":1}
    
    return render(request, 'producto/producto.html', {'form': form})

@login_required
def detalles(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
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