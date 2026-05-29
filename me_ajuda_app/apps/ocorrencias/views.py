from django.shortcuts import get_object_or_404, redirect, render
from intervencoes.models import Intervencao
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
    usuario = request.user.usuario
    is_cidadao = hasattr(usuario, 'cidadao')
    is_funcionario = hasattr(usuario, 'funcionario')
    
    if is_funcionario:
        ocorrencias = Ocorrencia.objects.all().order_by('-criado_em')
    elif is_cidadao:
        ocorrencias = Ocorrencia.objects.filter(cidadao=usuario.cidadao).order_by('criado_em')
    else:
        ocorrencias = Ocorrencia.objects.none()

    context = {
        'ocorrencias': ocorrencias,
        'is_funcionario': is_funcionario,
        'is_cidadao': is_cidadao,
    }
    
    return render(request, 'ocorrencia/ocorrencias_lista.html', context)

def atualizar_status(request, ocorrencia_id):
    usuario = request.user.usuario
    
    if request.method == 'POST' and hasattr(usuario, 'funcionario'):
        ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
        novo_status = request.POST.get('status')
        
        ocorrencia.status = novo_status
        ocorrencia.save()
                
    return redirect('ocorrencias:ocorrencias_lista')

def detalhar_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)

    context = {
        'ocorrencia': ocorrencia,
    }
    return render(request, 'ocorrencia/ocorrencia_detail.html', context)

@login_required
def painel_funcionario(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    abertas_count = Ocorrencia.objects.filter(status='ABE').count()
    andamento_count = Ocorrencia.objects.filter(status='AND').count()
    fechadas_count = Ocorrencia.objects.filter(status='FEC').count()
    
    intervencoes_count = Intervencao.objects.filter(funcionario__user=request.user).count()
    
    recentes = Ocorrencia.objects.select_related('servico').order_by('-criado_em')[:5]

    context = {
        'abertas': abertas_count,
        'em_andamento': andamento_count,
        'fechadas': fechadas_count,
        'intervencoes': intervencoes_count,
        'recentes': recentes,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'ocorrencia/painel.html', context)