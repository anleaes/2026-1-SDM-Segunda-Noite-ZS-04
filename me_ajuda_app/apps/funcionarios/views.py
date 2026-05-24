from django.shortcuts import render
from .models import Funcionario
from rest_framework import viewsets
from .serializer import FuncionarioSerializer


# Create your views here.
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer