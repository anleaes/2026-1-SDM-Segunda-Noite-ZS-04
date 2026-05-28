import re
from django import forms
from .models import Usuario
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        exclude = ['user']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        widgets = {'password': forms.PasswordInput(attrs={'id': 'id_senha'})}
        labels = {
            'password': 'Senha',
        }
