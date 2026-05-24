from django.shortcuts import render
from .models import Secretaria
from rest_framework import viewsets
from .serializer import SecretariaSerializer

# Create your views here.
class SecretariaViewSet(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer  