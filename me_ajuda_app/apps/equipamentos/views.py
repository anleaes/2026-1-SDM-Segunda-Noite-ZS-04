from django.shortcuts import render
from .models import Equipamento
from rest_framework import viewsets
from .serializer import EquipamentoSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer  

@login_required(login_url='/usuarios/login/')
def equipamentos_lista(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    equipamentos = Equipamento.objects.filter(disponivel=True).order_by('-id')

    context = {
        'equipamentos': equipamentos,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'equipamentos/equipamentos_lista.html', context)


from django.shortcuts import render, redirect
from .forms import EquipamentoForm

def equipamento_criar(request):

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamentos_lista')  
    else:
       
        form = EquipamentoForm()

    context = {
        'form': form,
    }
    
    return render(request, 'equipamentos/equipamento_form.html', context)