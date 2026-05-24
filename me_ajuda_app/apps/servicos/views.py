from django.shortcuts import render
from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer

# Create your views here.
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer  