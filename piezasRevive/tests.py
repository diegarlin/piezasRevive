from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import PerfilUsuario

class PiezasReviveViewsTests(TestCase):
    def setUp(self):
        # Crear un usuario de ejemplo
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)  # Redirigir a la página de productos

    def test_register_view(self):
        # Prueba GET en la vista de registro
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        # Prueba POST en la vista de registro con datos válidos
        data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'email': 'newuser@example.com',
            'forma_entrega': 'express',
            'forma_pago': 'contrareembolso',
            'domicilio': '123 Main St'
        }
        response = self.client.post(reverse('register'), data=data)
        
        # Imprimir información sobre el error
        print(response.content.decode('utf-8'))
        
       

    def test_login_view(self):
        # Prueba GET en la vista de inicio de sesión
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Prueba POST en la vista de inicio de sesión con credenciales válidas
        data = {'username': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)  # Redirigir después del inicio de sesión

    def test_logout_view(self):
        # Prueba POST en la vista de cierre de sesión
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirigir después del cierre de sesión
