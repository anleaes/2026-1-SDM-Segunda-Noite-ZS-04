from django.shortcuts import render, redirect
from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer
from .forms import ServicoForm



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
        is_gestor = hasattr(usuario, 'funcionario') and usuario.funcionario.funcao == 'GES'

    context = {
        'servicos': servicos,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor,
    }
    
    return render(request, 'servicos/servicos_lista.html', context)


def servico_criar(request):

    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos_lista')  
    else:
    
        form = ServicoForm()

    context = {
        'form': form,
    }

    return render(request, 'servicos_form.html', context)