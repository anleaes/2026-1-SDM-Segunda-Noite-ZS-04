from django.shortcuts import render
from .models import Ocorrencia
from rest_framework import viewsets
from .serializer import OcorrenciaSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer  
