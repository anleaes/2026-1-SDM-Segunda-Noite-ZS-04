from django.shortcuts import render
from .models import Ocorrencia
from rest_framework import viewsets
from .serializer import OcorrenciaSerializer

# Create your views here.
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer  
