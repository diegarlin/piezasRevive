from django.urls import path

from . import views

urlpatterns = [
    path("carrito/", views.ver_carrito, name="carrito"),
    path("agregar/<int:producto_id>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path("listar_productos/", views.listar_productos, name="listar_productos"),
]