from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Intervencao
from rest_framework import viewsets
from .serializer import IntervencaoSerializer
from .forms import IntervencaoForm

# Create your views here.
class IntervencaoViewSet(viewsets.ModelViewSet):
    queryset = Intervencao.objects.all()
    serializer_class = IntervencaoSerializer  

@login_required(login_url='/usuarios/login/')
def listar_intervencoes(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_gestor = usuario.funcionario.funcao == 'GES'
    intervencoes = Intervencao.objects.filter(funcionario=usuario.funcionario).order_by('-data_exec')

    context = {
        'intervencoes': intervencoes,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor,
    }
    return render(request, 'intervencoes/intervencoes_lista.html', context)

@login_required(login_url='/usuarios/login/')
def nova_intervencao(request):   
    if request.method == 'POST':
        form = IntervencaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('intervencoes:intervencoes_lista')
    else:
        form = IntervencaoForm()

    context = {
        'form': form,
        'acao': 'Nova',
    }
    return render(request, 'intervencoes/intervencao_form.html', context)

@login_required(login_url='/usuarios/login/')
def editar_intervencao(request, id):
    intervencao = get_object_or_404(Intervencao, id=id)

    if request.method == 'POST':
        form = IntervencaoForm(request.POST, request.FILES, instance=intervencao)
        if form.is_valid():
            form.save()
            return redirect('intervencoes:intervencoes_lista')
    else:
        form = IntervencaoForm(instance=intervencao)

    context = {
        'form': form,
        'acao': 'Editar',
    }
    return render(request, 'intervencoes/intervencao_form.html', context)