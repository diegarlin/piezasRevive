from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellidos")

    EXPRESS = 'express'
    NORMAL = 'normal'
    
    FORMA_ENTREGA = (
        (EXPRESS, 'express'),
        (NORMAL, 'normal'),     
    )

    forma_entrega = forms.ChoiceField(
        choices=FORMA_ENTREGA,
    )

    CONTRAREEMBOLSO = 'contrareembolso'
    TARJETA = 'tarjeta'

    FORMA_PAGO = (
        (CONTRAREEMBOLSO, 'contrareembolso'),
        (TARJETA, 'tarjeta'),     
    )

    forma_pago = forms.ChoiceField(
        choices=FORMA_PAGO,
    )

    domicilio = forms.CharField(max_length=30, required=True, label="Domicilio")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo electrónico.')
        return email
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'forma_pago', 'forma_entrega', 'domicilio']

class CorreoElectronicoAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}), label="Email")

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class EditarPerfilForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellidos")

    EXPRESS = 'express'
    NORMAL = 'normal'
    
    FORMA_ENTREGA = (
        (EXPRESS, 'express'),
        (NORMAL, 'normal'),     
    )

    forma_entrega = forms.ChoiceField(
        choices=FORMA_ENTREGA,
    )

    CONTRAREEMBOLSO = 'contrareembolso'
    TARJETA = 'tarjeta'

    FORMA_PAGO = (
        (CONTRAREEMBOLSO, 'contrareembolso'),
        (TARJETA, 'tarjeta'),     
    )

    forma_pago = forms.ChoiceField(
        choices=FORMA_PAGO,
    )

    domicilio = forms.CharField(max_length=30, required=True, label="Domicilio")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Excluir el usuario actual de la validación
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo electrónico.')
        return email
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'forma_entrega', 'forma_pago', 'domicilio']