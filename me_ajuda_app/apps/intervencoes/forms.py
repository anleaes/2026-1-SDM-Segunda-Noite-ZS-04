from django import forms
from .models import Intervencao

class IntervencaoForm(forms.ModelForm):

    class Meta:
        model = Intervencao
        exclude = () # Se necessário, especifique campos. Ex: fields = ['descricao', 'status']