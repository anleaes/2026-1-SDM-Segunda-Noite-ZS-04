from django.shortcuts import render
from .models import Secretaria
from rest_framework import viewsets
from .serializer import SecretariaSerializer

# Create your views here.
class SecretariaViewSet(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer  

def secretaria_lista(request):

    if request.user.is_authenticated:
        usuario = request.user.usuario
        is_funcionario = hasattr(usuario, 'funcionario')
        is_cidadao = hasattr(usuario, 'cidadao')

    secretarias = Secretaria.objects.all().order_by('nome')
    
    context = {
        'secretarias': secretarias,
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'secretaria/secretarias_lista.html', context)