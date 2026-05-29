from django.shortcuts import render
from .models import Intervencao
from rest_framework import viewsets
from .serializer import IntervencaoSerializer

# Create your views here.
class IntervencaoViewSet(viewsets.ModelViewSet):
    queryset = Intervencao.objects.all()
    serializer_class = IntervencaoSerializer  

    def listar_intervencoes(request):
    # Busca todas as intervenções do banco de dados
    # Ordenado pelas mais recentes (ajuste o campo de data se necessário)
    intervencoes = Intervencao.objects.all().order_by('-id')

    context = {
        'intervencoes': intervencoes,
    }
    return render(request, 'intervencoes/intervencoes_lista.html', context)