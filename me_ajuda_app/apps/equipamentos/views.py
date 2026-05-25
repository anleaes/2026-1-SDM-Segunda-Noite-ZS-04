from django.shortcuts import render
from .models import Equipamento
from rest_framework import viewsets
from .serializer import EquipamentoSerializer

# Create your views here.
class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer  