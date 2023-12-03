from django.urls import path
from . import views

app_name="opinion"

urlpatterns = [
    path('crear_opinion/<int:producto_id>', views.crear_opinion, name='crear_opinion'),
]