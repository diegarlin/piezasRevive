from django.urls import path
from . import views


app_name="reclamaciones"

urlpatterns = [
    path('detalle_reclamacion/<int:reclamacion_id>/', views.detalle_reclamacion, name='detalle_reclamacion'),
    path("reclamaciones/<int:pedido_id>/", views.crear_reclamacion, name='crear_reclamacion'),
    path('ingresar_correo/<int:pedido_id>/', views.ingresar_correo, name='ingresar_correo'),
    path("reclamacion/<int:pedido_id>/", views.crear_reclamacion_sinloguear, name='crear_reclamacion_sinloguear'),
    path('listar_reclamaciones_pedido/<int:pedido_id>/', views.listar_reclamaciones_pedido, name='listar_reclamaciones_pedido'),
]