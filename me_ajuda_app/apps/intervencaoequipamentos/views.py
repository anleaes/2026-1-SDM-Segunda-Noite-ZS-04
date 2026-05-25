from django.shortcuts import render
from .models import IntervencaoEquipamento
from rest_framework import viewsets
from .serializer import IntervencaoEquipamentoSerializer

# Create your views here.
class IntervencaoEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = IntervencaoEquipamento.objects.all()
    serializer_class = IntervencaoEquipamentoSerializer  