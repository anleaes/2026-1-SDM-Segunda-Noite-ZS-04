from django.shortcuts import render,redirect, get_object_or_404
from .models import Funcionario
from rest_framework import viewsets
from .serializer import FuncionarioSerializer
from django.contrib.auth.decorators import login_required
from funcionarios.forms import FuncionarioForm


# Create your views here.
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

@login_required(login_url='/usuarios/login/')
def lista_funcionarios(request):
    template_name = 'funcionarios/lista_funcionarios.html'
    usuario = request.user

    if not usuario.is_superuser:
        return redirect('core:home') 
     
    funcionarios = Funcionario.objects.all().order_by('id')

    context = {
        'funcionarios': funcionarios
    }
    
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def excluir_funcionario(request, funcionario_id):
    usuario = request.user

    if not usuario.is_superuser:
        return redirect('core:home') 
    
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    funcionario.user.delete()
        
    return redirect('funcionarios:lista_funcionarios')