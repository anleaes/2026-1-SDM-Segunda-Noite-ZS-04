from django import forms
from .models import Intervencao


class IntervencaoForm(forms.ModelForm):

    class Meta:
        model = Intervencao
        exclude = ['funcionario', 'ocorrencia']

        widgets = {
            'data_exec': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'
            ),
        }
