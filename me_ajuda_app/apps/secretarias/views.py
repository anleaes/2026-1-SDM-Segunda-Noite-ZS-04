from django.shortcuts import render, redirect
from .models import Secretaria
from rest_framework import viewsets
from .serializer import SecretariaSerializer
from .forms import SecretariaForm

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

def secretaria_criar(request):
    
    if request.method == 'POST':
        form = SecretariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secretarias:secretarias_lista')  
    else:
        
        form = SecretariaForm()

    context = {
        'form': form,
    }
    
    return render(request, 'secretaria/secretaria_form.html', context)