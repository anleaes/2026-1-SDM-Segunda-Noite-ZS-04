from django.shortcuts import render, redirect, get_object_or_404
from .models import Secretaria
from rest_framework import viewsets
from .serializer import SecretariaSerializer
from .forms import SecretariaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class SecretariaViewSet(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer  

def secretaria_lista(request):
    is_funcionario = False
    is_cidadao = False
    is_gestor = False

    if request.user.is_authenticated:
        usuario = request.user.usuario
        is_funcionario = hasattr(usuario, 'funcionario')
        is_cidadao = hasattr(usuario, 'cidadao')
        is_gestor = hasattr(usuario, 'funcionario') and usuario.funcionario.funcao == 'GES'

    secretarias = Secretaria.objects.all().order_by('nome')
    
    context = {
        'secretarias': secretarias,
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor,
    }
    
    return render(request, 'secretarias/lista_secretarias.html', context)

@login_required(login_url='/usuarios/login/')
def secretaria_criar(request):
    
    if request.method == 'POST':
        form = SecretariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secretarias:secretaria_lista')  
    else:
        
        form = SecretariaForm()

    context = {
        'form': form,
    }
    
    return render(request, 'secretarias/criar_secretaria.html', context)

def editar_secretaria(request, id_secretaria):
    template_name = 'secretarias/editar_secretaria.html'
    context ={}
    secretaria = get_object_or_404(Secretaria, id=id_secretaria)
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if request.method == 'POST':
        form = SecretariaForm(request.POST, instance=secretaria)
        if form.is_valid():
            form.save()
            return redirect('secretarias:secretaria_lista')
    else:
        form = SecretariaForm(instance=secretaria)

    context = {
        'form': form,
        'secretaria': secretaria,
        'is_funcionario': is_funcionario,
    }

    return render(request, template_name, context)

def excluir_secretaria(request, id_secretaria):
    secretaria = Secretaria.objects.get(id=id_secretaria)
    secretaria.delete()
    
    return redirect('secretarias:secretaria_lista')