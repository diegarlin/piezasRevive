from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product, name='product'),
    path('product/details/<int:product_id>', views.detalles, name='detalles'),
    path('product/name/', views.nombre, name='nombre'),
    
    path('product/name/search', views.search_by_name, name='search_by_name'),
    
    #path('category/', views.category, name='category'),
   # path('category/search-by-<category>', views.search_by_category, name='search_by_category'),
    
    #path('brand/', views.brand, name='brand'),
   # path('brand/search-by-<brand>', views.search_by_brand, name='search_by_brand'),
    
]