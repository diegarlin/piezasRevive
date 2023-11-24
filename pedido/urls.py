from django.urls import path
from . import views


app_name="pedidos"

urlpatterns = [

    path('procesarPedido/', views.procesar_pedido, name='procesar_pedido'),
    path('hacerPedido/', views.hacer_pedido, name='hacer_pedido'),
    path('buscarPedido/', views.buscar_pedido, name='buscar_pedido'),
    path('mostrarPedido/', views.mostrar_pedido, name='mostrar_pedido')
]