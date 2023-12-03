from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import Categorias, Marcas, detalles
from .models import Producto
from opinion.models import Opinion
from django.contrib.auth.models import User

class ProductTestCase(TestCase):
    def test_product_view(self):
        # Create a test request with the necessary GET parameters
        response = self.client.get(reverse('product'), {'nombre': 'test', 'categoria': 'Freno', 'marca': 'Seat'})
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert that the 'marca_buscada' value is printed
        self.assertContains(response, 'Seat')
        
        # Assert that the 'lista_tuplas_productos' value is passed to the template context
        self.assertEqual(response.context['tupla_producto'], [])
        
        # Assert that the 'modelmap' values are passed to the template context
        self.assertEqual(response.context['categorias'], Categorias)
        self.assertEqual(response.context['marcas'], Marcas)
        
        # Assert that the correct template is used for rendering
        self.assertTemplateUsed(response, 'producto/producto.html')
    
    def setUp(self):
        self.factory = RequestFactory()
        self.producto = Producto.objects.create(nombre='Test Product', categoria='Embrague', marca='Seat', stock=10, precio=100, imagen='test.jpg', descripcion='Test Description')
        self.opinion1 = Opinion.objects.create(producto=self.producto, comentario='Opinion 1', usuario=User.objects.create_user(username='testuser1'))
        self.opinion2 = Opinion.objects.create(producto=self.producto, comentario='Opinion 2', usuario=User.objects.create_user(username='testuser2'))

    def test_detalles(self):
        response = self.client.get(f'/product/details/{self.producto.id}')
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'producto/productoDetalles.html')
        self.assertEqual(response.context['producto'], self.producto)
        self.assertEqual(response.context['opiniones'], [self.opinion1, self.opinion2])