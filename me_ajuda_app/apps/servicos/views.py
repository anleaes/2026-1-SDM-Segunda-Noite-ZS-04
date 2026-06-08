from django.shortcuts import render, redirect, get_object_or_404
from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer
from .forms import ServicoForm
from django.contrib.auth.decorators import login_required



# Create your views here.
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer  

def lista_servicos(request):

    query = request.GET.get('q', '')
    
    if query:
        busca_nome = Servico.objects.filter(nome__icontains=query)
        busca_desc = Servico.objects.filter(descricao__icontains=query)
        
        servicos = (busca_nome | busca_desc).distinct().order_by('nome')
    else:
        servicos = Servico.objects.all().order_by('nome')
       
    is_funcionario = False
    is_gestor = False
    
    if request.user.is_authenticated:
        usuario = request.user.usuario
        is_funcionario = hasattr(usuario, 'funcionario')
        is_cidadao = hasattr(usuario, 'cidadao')
        is_gestor = hasattr(usuario, 'funcionario') and usuario.funcionario.funcao == 'GES'

    context = {
        'servicos': servicos,
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor,
    }
    
    return render(request, 'servicos/lista_servicos.html', context)

@login_required(login_url='/usuarios/login/')
def criar_servico(request):

    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos:lista_servicos')  
    else:
        form = ServicoForm()

    context = {
        'form': form,
        'is_funcionario': is_funcionario,
    }

    return render(request, 'servicos/criar_servico.html', context)

@login_required(login_url='/usuarios/login/')
def editar_servico(request, id_servico):
    template_name = 'servicos/editar_servico.html'
    context ={}
    servico = get_object_or_404(Servico, id=id_servico)
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servicos:lista_servicos')
    else:
        form = ServicoForm(instance=servico)

    context = {
        'form': form,
        'servico': servico,
        'is_funcionario': is_funcionario,
    }

    return render(request, template_name, context)

def excluir_servico(request, id_servico):
    servico = Servico.objects.get(id=id_servico)
    servico.delete()
    
    return redirect('servicos:lista_servicos')