from django import forms
from django.urls import path
from .models import Cidadao

class CidadaoForm(forms.ModelForm):

    class Meta:
        model = Cidadao
        exclude = ()