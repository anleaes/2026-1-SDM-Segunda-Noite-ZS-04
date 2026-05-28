from django.shortcuts import render
from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer

# Create your views here.
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer  

def servicos_lista(request):
    # Busca todos os serviços ativos no sistema
    # Se o seu modelo tiver um campo 'ativo', descomente a linha abaixo:
    # servicos = Servico.objects.filter(ativo=True).order_by('nome')
    
    servicos = Servico.objects.all().order_by('nome')
    
    # Identifica o tipo de usuário caso precise ocultar/exibir botões no HTML
    is_funcionario = hasattr(request.user, 'funcionario')

    context = {
        'servicos': servicos,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'servicos/servicos_lista.html', context)