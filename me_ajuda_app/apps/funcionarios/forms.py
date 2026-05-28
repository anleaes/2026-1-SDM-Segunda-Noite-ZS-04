from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['registro', 'funcao', 'ativo', 'secretarias']
        widgets = {
            'secretarias': forms.CheckboxSelectMultiple(),
        }