from django import forms
from .models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        exclude = ['criado_em', 'fechado_em', 'status', 'cidadao']
        
