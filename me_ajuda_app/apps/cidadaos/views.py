from django.shortcuts import render
from .models import Cidadao
from rest_framework import viewsets
from .serializer import CidadaoSerializer

# Create your views here.
class CidadaoViewSet(viewsets.ModelViewSet):
    queryset = Cidadao.objects.all()
    serializer_class = CidadaoSerializer  