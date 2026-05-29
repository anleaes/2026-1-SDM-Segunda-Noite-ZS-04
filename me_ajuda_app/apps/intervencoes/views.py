from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from me_ajuda_app.apps.equipamentos.models import Equipamento
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
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario') 

    if request.method == 'POST':
        form = IntervencaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('intervencoes:intervencoes_lista')
    else:
        form = IntervencaoForm()

    context = {
        'form': form,
        'is_funcionario': is_funcionario,
    }
    return render(request, 'intervencoes/intervencoes_forms.html', context)

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
    return render(request, 'intervencoes/intervencoes_forms.html', context)

@login_required
def alocacao_equipamentos(request):
    cart = request.session.get('cart_equipamentos', {})
    total = 0.0
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    for id, item in cart.items():
        total += float(item['custo_total'])
    context = {
        'cart': cart,
        'total': total,
        'is_funcionario': is_funcionario,
    }

    return render(request, 'intervencoes/intervencoes_alocacao.html', context)

@login_required
def add_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id=equipamento_id)
    cart = request.session.get('cart_equipamentos', {})
    eid = str(equipamento.id)
    
    if eid in cart:
        cart[eid]['horas_usado'] += 1
    else:
        cart[eid] = {
            'nome': equipamento.nome,
            'preco': float(equipamento.preco),
            'horas_usado': 1,
            'custo_total': float(equipamento.preco),
        }
        
    horas = cart[eid]['horas_usado']
    preco = float(cart[eid]['preco'])
    cart[eid]['custo_total'] = preco * horas
    
    request.session['cart_equipamentos'] = cart
    request.session.modified = True
    return redirect('intervencoes:alocacao_equipamentos')