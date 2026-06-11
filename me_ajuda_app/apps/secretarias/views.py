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

def lista_secretarias(request):
    template_name = 'secretarias/lista_secretarias.html'
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
    
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def criar_secretaria(request):
    template_name = 'secretarias/criar_secretaria.html'
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    
    if request.method == 'POST':
        form = SecretariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secretarias:lista_secretarias')  
    else:
        
        form = SecretariaForm()

    context = {
        'form': form,
        'is_funcionario': is_funcionario
    }
    
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def editar_secretaria(request, secretaria_id):
    template_name = 'secretarias/editar_secretaria.html'
    secretaria = get_object_or_404(Secretaria, id=secretaria_id)
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if request.method == 'POST':
        form = SecretariaForm(request.POST, instance=secretaria)
        if form.is_valid():
            form.save()
            return redirect('secretarias:lista_secretarias')
    else:
        form = SecretariaForm(instance=secretaria)

    context = {
        'form': form,
        'secretaria': secretaria,
        'is_funcionario': is_funcionario,
    }

    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def excluir_secretaria(request, secretaria_id):
    secretaria = Secretaria.objects.get(id=secretaria_id)
    secretaria.delete()
    
    return redirect('secretarias:lista_secretarias')