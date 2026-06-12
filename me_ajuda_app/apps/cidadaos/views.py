from django.shortcuts import render,redirect, get_object_or_404
from .models import Cidadao
from rest_framework import viewsets
from .serializer import CidadaoSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class CidadaoViewSet(viewsets.ModelViewSet):
    queryset = Cidadao.objects.all()
    serializer_class = CidadaoSerializer  

@login_required(login_url='/usuarios/login/')
def lista_cidadaos(request):
    template_name = 'cidadaos/lista_cidadaos.html'
    usuario = request.user

    if not usuario.is_superuser:
        return redirect('core:home') 
     
    cidadaos = Cidadao.objects.all().order_by('id')

    context = {
        'cidadaos': cidadaos
    }
    
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def excluir_cidadao(request, cidadao_id):
    usuario = request.user

    if not usuario.is_superuser:
        return redirect('core:home') 
    
    cidadao = get_object_or_404(Cidadao, id=cidadao_id)
    cidadao.user.delete()
        
    return redirect('cidadaos:lista_cidadaos')