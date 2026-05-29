from django.shortcuts import render, redirect
from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer
from .forms import ServicoForm
from django.contrib.auth.decorators import login_required



# Create your views here.
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer  

def servicos_lista(request):

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
    
    return render(request, 'servicos/servicos_lista.html', context)

@login_required(login_url='/usuarios/login/')
def servico_criar(request):

    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos:servicos_lista')  
    else:
        form = ServicoForm()

    context = {
        'form': form,
        'is_funcionario': is_funcionario,
    }

    return render(request, 'servicos/servicos_form.html', context)