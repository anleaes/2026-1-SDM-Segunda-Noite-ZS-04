from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from equipamentos.models import Equipamento
from intervencaoequipamentos.models import IntervencaoEquipamento
from .models import Intervencao
from rest_framework import viewsets
from .serializer import IntervencaoSerializer
from .forms import IntervencaoForm

# Create your views here.
class IntervencaoViewSet(viewsets.ModelViewSet):
    queryset = Intervencao.objects.all()
    serializer_class = IntervencaoSerializer  

@login_required(login_url='/usuarios/login/')
def lista_intervencoes(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_gestor = usuario.funcionario.funcao == 'GES'
    intervencoes = Intervencao.objects.filter(funcionario=usuario.funcionario).order_by('-data_exec')

    context = {
        'intervencoes': intervencoes,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor,
    }
    return render(request, 'intervencoes/lista_intervencoes.html', context)

@login_required(login_url='/usuarios/login/')
def lista_equipamentos_intervencao(request):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    equipamentos = Equipamento.objects.all().order_by('nome')

    context = {
        'equipamentos': equipamentos,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'intervencoes/lista_equipamentos_intervencao.html', context)

@login_required(login_url='/usuarios/login/')
def criar_intervencao(request, ocorrencia_id=None):  
    cart = request.session.get('cart_equipamentos', {}) 
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')

    if ocorrencia_id:
        request.session['ocorrencia_atual'] = ocorrencia_id
    else:
        ocorrencia_id = request.session.get('ocorrencia_atual')

    total_equipamentos = 0.0
    for equipamento_id, item in cart.items():
        total_equipamentos += float(item.get('custo_total', 0))

    if request.method == 'POST':
        form = IntervencaoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.funcionario = request.user.usuario.funcionario
            if ocorrencia_id:
                f.ocorrencia_id = ocorrencia_id
            intervencao = form.save()
            
            for equipamento_id, item in cart.items():
                equipamento = Equipamento.objects.get(id=equipamento_id)
                IntervencaoEquipamento.objects.create(
                    intervencao=intervencao,
                    equipamento=equipamento,
                    horas_usado=int(item['horas_usado']),
                    custo_total=float(item['custo_total'])
                )
            
            request.session['cart_equipamentos'] = {}
            request.session.modified = True
            
            return redirect('intervencoes:intervencoes_lista')
    else:
        form = IntervencaoForm()

    context = {
        'form': form,
        'cart': cart,
        'total_equipamentos': total_equipamentos,
        'is_funcionario': is_funcionario,
        'ocorrencia_id': ocorrencia_id,
    }
    
    return render(request, 'intervencoes/criar_intervencao.html', context)

@login_required(login_url='/usuarios/login/')
def editar_intervencao(request, id):
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
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
        'is_funcionario': is_funcionario,
    }
    return render(request, 'intervencoes/criar_intervencao.html', context)

@login_required(login_url='/usuarios/login/')
def alocacao_equipamentos(request):
    cart = request.session.get('cart_equipamentos', {})
    total = 0.0
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    
    for equipamento_id, item in cart.items():
        total += float(item['custo_total'])
    context = {
        'cart': cart,
        'total': total,
        'is_funcionario': is_funcionario,
    }

    return render(request, 'intervencoes/alocacao_intervencao.html', context)

@login_required(login_url='/usuarios/login/')
def adicionar_alocacao(request, equipamento_id):
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

@login_required(login_url='/usuarios/login/')
def editar_alocacao(request, equipamento_id):
    if request.method == 'POST':
        horas = int(request.POST.get('horas_usado', 1))
        cart = request.session.get('cart_equipamentos', {})
        eid = str(equipamento_id)
        
        if eid in cart:
            if horas <= 0:
                del cart[eid]
            else:
                preco = float(cart[eid]['preco'])
                cart[eid]['horas_usado'] = horas
                cart[eid]['custo_total'] = preco * horas
                
        request.session['cart_equipamentos'] = cart
        request.session.modified = True
    return redirect('intervencoes:alocacao_equipamentos')

@login_required(login_url='/usuarios/login/')
def excluir_alocacao(request, equipamento_id):
    cart = request.session.get('cart_equipamentos', {})
    eid = str(equipamento_id)
    if eid in cart:
        del cart[eid]
    request.session['cart_equipamentos'] = cart
    request.session.modified = True
    return redirect('intervencoes:alocacao_equipamentos')