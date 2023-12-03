from django.urls import path

from .import views

app_name="pagos"

urlpatterns = [
        path('pagos/', views.home, name='home'),
        path('pagos/create-checkout-session/', views.create_checkout_session, name='checkout'),
        path('pagos/success/', views.success,name='success'),
        path('pagos/cancel/', views.cancel,name='cancel'),
]