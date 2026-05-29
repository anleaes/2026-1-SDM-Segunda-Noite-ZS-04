from datetime import timedelta
from django.shortcuts import render
from .models import Protocolo
from rest_framework import viewsets
from .serializer import ProtocoloSerializer
# Create your views here.
class ProtocoloViewSet(viewsets.ModelViewSet):
    queryset = Protocolo.objects.all()
    serializer_class = ProtocoloSerializer 

def protocolo_criar(ocorrencia):
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