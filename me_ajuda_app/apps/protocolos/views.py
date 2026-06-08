from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Protocolo
from rest_framework import viewsets
from .serializer import ProtocoloSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class ProtocoloViewSet(viewsets.ModelViewSet):
    queryset = Protocolo.objects.all()
    serializer_class = ProtocoloSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ocorrencia']

def criar_protocolo(ocorrencia):
    if hasattr(ocorrencia, 'protocolo'):
        return ocorrencia.protocolo
    
    agora = ocorrencia.criado_em
    
    numero_protocolo = f"{agora.strftime('%Y%m%d')}-{ocorrencia.id:06d}"
    
    return Protocolo.objects.create(
        ocorrencia=ocorrencia,
        protocolo_numero=numero_protocolo,
        gerado_em=agora,
        prazo=agora.date() + timedelta(days=15)
    )

@login_required(login_url='/usuarios/login/')
def ver_protocolo(request, protocolo_id):
    template_name = 'protocolos/ver_protocolo.html'
    protocolo = get_object_or_404(Protocolo, id=protocolo_id)
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_cidadao = hasattr(usuario, 'cidadao')

    context = {
        'protocolo': protocolo,
        'is_funcionario': is_funcionario,
        'is_cidadao': is_cidadao,
    }
    
    return render(request, template_name, context)