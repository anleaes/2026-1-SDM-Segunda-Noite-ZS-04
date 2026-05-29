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
   
    servicos = Servico.objects.all().order_by('nome')
    
    is_funcionario = False
    if request.user.is_authenticated:
        is_funcionario = hasattr(request.user, 'funcionario')

    # 3. Monta o contexto para enviar ao HTML
    context = {
        'servicos': servicos,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'servicos/servicos_lista.html', context)


def servico_criar(request):
    # Verifica se a requisição é um envio de dados (POST)
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireciona de volta para a lista de serviços após salvar
            return redirect('ocorrencias:servicos_lista')
    else:
        # Se for um acesso normal (GET), entrega o formulário vazio
        form = ServicoForm()

    context = {
        'form': form,
    }
    
    return render(request, 'servicos_form.html', context)