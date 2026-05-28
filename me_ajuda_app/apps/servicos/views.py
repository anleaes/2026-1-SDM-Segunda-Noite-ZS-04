from django.shortcuts import render
from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer

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