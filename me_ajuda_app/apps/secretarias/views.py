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
    
    context = {
        'secretarias': secretarias,
    }
    
    return render(request, 'secretaria/secretarias_lista.html', context)