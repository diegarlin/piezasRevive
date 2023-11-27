from django.urls import path
from . import views


app_name="reclamaciones"

urlpatterns = [
    path('detalle_reclamacion/<int:reclamacion_id>/', views.detalle_reclamacion, name='detalle_reclamacion'),
    path("reclamaciones/<int:pedido_id>/", views.crear_reclamacion, name='crear_reclamacion'),

]