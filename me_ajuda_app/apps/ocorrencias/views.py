from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from intervencoes.models import Intervencao
from protocolos.views import criar_protocolo
from .models import Ocorrencia
from rest_framework import viewsets
from .serializer import OcorrenciaSerializer
from django.contrib.auth.decorators import login_required
from .forms import OcorrenciaForm

# Create your views here.
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer  

@login_required(login_url='/usuarios/login/')
def lista_ocorrencias(request):
    usuario = request.user.usuario
    is_cidadao = hasattr(usuario, 'cidadao')
    is_funcionario = hasattr(usuario, 'funcionario')
    
    if is_funcionario:
        secretarias = usuario.funcionario.secretarias.all()
        ocorrencias = Ocorrencia.objects.filter(servico__secretaria__in=secretarias).order_by('-criado_em')
    elif is_cidadao:
        ocorrencias = Ocorrencia.objects.filter(cidadao=usuario.cidadao).order_by('-criado_em')
    else:
        ocorrencias = Ocorrencia.objects.none()

    context = {
        'ocorrencias': ocorrencias,
        'is_funcionario': is_funcionario,
        'is_cidadao': is_cidadao,
    }
    
    return render(request, 'ocorrencias/lista_ocorrencias.html', context)

@login_required(login_url='/usuarios/login/')
def atualizar_status_ocorrencia(request, ocorrencia_id):
    usuario = request.user.usuario
    
    if request.method == 'POST' and hasattr(usuario, 'funcionario'):
        ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
        novo_status = request.POST.get('status')

        if novo_status == 'FEC':
            ocorrencia.fechado_em = timezone.now()
        else:            
            ocorrencia.fechado_em = None
        
        ocorrencia.status = novo_status
        ocorrencia.save()
                
    return redirect('ocorrencias:lista_ocorrencias')

@login_required(login_url='/usuarios/login/')
def ver_ocorrencia(request, ocorrencia_id):
    usuario = request.user.usuario
    is_cidadao = hasattr(usuario, 'cidadao')
    is_funcionario = hasattr(usuario, 'funcionario')
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)

    context = {
        'ocorrencia': ocorrencia,
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
    }
    return render(request, 'ocorrencias/ver_ocorrencia.html', context)

@login_required(login_url='/usuarios/login/')
def painel_ocorrencias(request):
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
    
    return render(request, 'ocorrencias/painel_ocorrencias.html', context)

@login_required(login_url='/usuarios/login/')
def criar_ocorrencia(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_cidadao = hasattr(usuario, 'cidadao')

    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.cidadao = usuario.cidadao
            f.status = 'ABE'
            f.save()
            criar_protocolo(f)
            return redirect('ocorrencias:lista_ocorrencias')  
    else:
        form = OcorrenciaForm()
        servico_id = request.GET.get('servico_id')
        if servico_id:
            form.fields['servico'].initial = servico_id

    context = {
        'form': form,
        'is_funcionario': is_funcionario,
        'is_cidadao': is_cidadao,
    }

    return render(request, 'ocorrencias/criar_ocorrencia.html', context)

@login_required(login_url='/usuarios/login/')
def editar_ocorrencia(request, ocorrencia_id):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_cidadao = hasattr(usuario, 'cidadao')
    ocorrencia =  get_object_or_404(Ocorrencia, id=ocorrencia_id)
    template_name = 'ocorrencias/editar_ocorrencia.html'

    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return redirect('ocorrencias:lista_ocorrencias')  
    else:
        form = OcorrenciaForm(instance=ocorrencia)

    context = {
        'form': form,
        'ocorrencia': ocorrencia,
        'is_funcionario': is_funcionario,
        'is_cidadao': is_cidadao,
    }

    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def excluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
    
    if request.method == 'POST':
        ocorrencia.delete()
        
    return redirect('ocorrencias:lista_ocorrencias')