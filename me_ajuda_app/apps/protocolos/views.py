from django.shortcuts import render
from .models import Protocolo
from rest_framework import viewsets
from .serializer import ProtocoloSerializer
# Create your views here.
class ProtocoloViewSet(viewsets.ModelViewSet):
    queryset = Protocolo.objects.all()
    serializer_class = ProtocoloSerializer 