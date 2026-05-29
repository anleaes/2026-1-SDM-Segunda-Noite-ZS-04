from django.shortcuts import render
from .models import Ocorrencia
from rest_framework import viewsets
from .serializer import OcorrenciaSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer  

@login_required(login_url='/usuarios/login/')
def ocorrencias_lista(request):
    # Identifica o tipo de usuário logado
    is_cidadao = hasattr(request.user, 'cidadao')
    is_funcionario = hasattr(request.user, 'funcionario')
    
    if is_funcionario:
        # Funcionários visualizam todas as ocorrências do sistema
        ocorrencias = Ocorrencia.objects.all().order_by('-data_criacao') # ou o campo de data do seu modelo
    elif is_cidadao:
        # Cidadãos visualizam apenas as ocorrências criadas por eles mesmos
        # (Ajuste 'usuario' ou 'cidadao' dependendo de como está a ForeignKey no seu modelo Ocorrencia)
        ocorrencias = Ocorrencia.objects.filter(usuario=request.user.usuario).order_by('-data_criacao')
    else:
        ocorrencias = Ocorrencia.objects.none()

    context = {
        'ocorrencias': ocorrencias,
        'is_funcionario': is_funcionario,
        'is_cidadao': is_cidadao,
    }
    
    return render(request, 'ocorrencias_lista.html', context)

def listar_ocorrencias(request):
    # Busca todas as ocorrências no banco de dados. 
    # Você pode adicionar .order_by('-id') para mostrar as mais recentes primeiro
    ocorrencias = Ocorrencia.objects.all()

    context = {
        'ocorrencias': ocorrencias,
    }
    return render(request, 'ocorrencias/listar_ocorrencias.html', context)