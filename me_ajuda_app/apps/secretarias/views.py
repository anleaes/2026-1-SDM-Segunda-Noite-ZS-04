from django.shortcuts import render
from .models import Secretaria
from rest_framework import viewsets
from .serializer import SecretariaSerializer

# Create your views here.
class SecretariaViewSet(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer  

def secretaria_lista(request):

    secretarias = Secretaria.objects.all().order_by('nome')
    
    is_funcionario = False
    if request.user.is_authenticated:
        is_funcionario = hasattr(request.user, 'funcionario')

    context = {
        'secretarias': secretarias,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'secretaria_lista.html', context)