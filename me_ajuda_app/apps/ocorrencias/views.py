from django.shortcuts import get_object_or_404, render
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
        ocorrencias = Ocorrencia.objects.all().order_by('criado_em')
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

def detalhar_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)

    context = {
        'ocorrencia': ocorrencia,
    }
    return render(request, 'ocorrencia/ocorrencia_detail.html', context)