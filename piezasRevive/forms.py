from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo electrónico.')
        return email
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class CorreoElectronicoAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']