from django.shortcuts import render
from .models import Intervencao
from rest_framework import viewsets
from .serializer import IntervencaoSerializer

# Create your views here.
class IntervencaoViewSet(viewsets.ModelViewSet):
    queryset = Intervencao.objects.all()
    serializer_class = IntervencaoSerializer  