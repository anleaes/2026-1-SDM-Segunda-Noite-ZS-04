from django import forms
from .models import Intervencao

class IntervencaoForm(forms.ModelForm):

    class Meta:
        model = Intervencao
        exclude = ['funcionario', 'ocorrencia']