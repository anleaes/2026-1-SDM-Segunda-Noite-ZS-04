from django import forms
from .models import Secretaria

class SecretariaForm(forms.ModelForm):

    class Meta:
        model = Secretaria
        exclude = ()  