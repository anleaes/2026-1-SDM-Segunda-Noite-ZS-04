from django.shortcuts import render,redirect, get_object_or_404
from .models import Equipamento
from rest_framework import viewsets
from .serializer import EquipamentoSerializer
from django.contrib.auth.decorators import login_required
from .forms import EquipamentoForm

# Create your views here.
class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer  

@login_required(login_url='/usuarios/login/')
def lista_equipamentos(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_gestor = usuario.funcionario.funcao == 'GES'
    equipamentos = Equipamento.objects.all().order_by('nome')

    context = {
        'equipamentos': equipamentos,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor
    }
    
    return render(request, 'equipamentos/lista_equipamentos.html', context)

@login_required(login_url='/usuarios/login/')
def criar_equipamento(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamentos:lista_equipamentos')  
    else:
       
        form = EquipamentoForm()

    context = {
        'form': form,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'equipamentos/criar_equipamento.html', context)

@login_required(login_url='/usuarios/login/')
def editar_equipamento(request, equipamento_id):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    equipamento =  get_object_or_404(Equipamento, id=equipamento_id)

    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipamentos:lista_equipamentos')  
    else:
        form = EquipamentoForm(instance=equipamento)

    context = {
        'form': form,
        'equipamento': equipamento,
        'is_funcionario': is_funcionario,
    }

    return render(request, 'equipamentos/editar_equipamento.html', context)

@login_required(login_url='/usuarios/login/')
def excluir_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id=equipamento_id)
    equipamento.delete()
        
    return redirect('equipamentos:lista_equipamentos')