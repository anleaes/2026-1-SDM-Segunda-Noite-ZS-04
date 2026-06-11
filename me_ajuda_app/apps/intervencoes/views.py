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
    template_name = 'intervencoes/lista_intervencoes.html'
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    is_gestor = usuario.funcionario.funcao == 'GES'
        
    if is_gestor:
        intervencoes = Intervencao.objects.all().order_by('-data_exec')
    else:
        intervencoes = Intervencao.objects.filter(funcionario=usuario.funcionario).order_by('-data_exec')

    context = {
        'intervencoes': intervencoes,
        'is_funcionario': is_funcionario,
        'is_gestor': is_gestor,
    }
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def lista_equipamentos_intervencao(request):
    template_name = 'intervencoes/lista_equipamentos_intervencao.html'     
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    equipamentos = Equipamento.objects.all().order_by('nome')
    equipamentos_disponiveis = [e for e in equipamentos if e.disponivel]   
    equipamentos = equipamentos_disponiveis 

    context = {
        'equipamentos': equipamentos,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def criar_intervencao(request, ocorrencia_id=None):  
    template_name = 'intervencoes/criar_intervencao.html'
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

            f.save()
            
            for equipamento_id, item in cart.items():
                equipamento = Equipamento.objects.get(id=equipamento_id)
                IntervencaoEquipamento.objects.create(
                    intervencao=f,
                    equipamento=equipamento,
                    horas_usado=int(item['horas_usado']),
                    custo_total=float(item['custo_total'])
                )
            
            request.session['cart_equipamentos'] = {}
            if 'ocorrencia_atual' in request.session:
                del request.session['ocorrencia_atual']

            request.session.modified = True
            
            return redirect('intervencoes:lista_intervencoes')
    else:
        form = IntervencaoForm()
        if total_equipamentos:
            form.fields['custo_trab'].initial = total_equipamentos

    context = {
        'form': form,
        'cart': cart,
        'total_equipamentos': total_equipamentos,
        'is_funcionario': is_funcionario,
        'ocorrencia_id': ocorrencia_id,
    }
    
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def editar_intervencao(request, intervencao_id):
    template_name = 'intervencoes/editar_intervencao.html'
    usuario = request.user.usuario
    is_funcionario = hasattr(usuario, 'funcionario')
    intervencao = get_object_or_404(Intervencao, id=intervencao_id)

    if request.method == 'POST':
        form = IntervencaoForm(request.POST, request.FILES, instance=intervencao)
        if form.is_valid():
            form.save()
            return redirect('intervencoes:lista_intervencoes')
    else:
        form = IntervencaoForm(instance=intervencao)

    context = {
        'form': form,
        'intervencao': intervencao,
        'is_funcionario': is_funcionario,
    }
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def alocacao_equipamentos(request):
    template_name = 'intervencoes/alocacao_equipamentos.html'
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

    return render(request, template_name, context)

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

@login_required(login_url='/usuarios/login/')
def ver_intervencao(request, intervencao_id):
    template_name = 'intervencoes/ver_intervencao.html'
    usuario = request.user.usuario
    is_cidadao = hasattr(usuario, 'cidadao')
    is_funcionario = hasattr(usuario, 'funcionario')
    intervencao = get_object_or_404(Intervencao, id=intervencao_id)
    equipamentos = intervencao.equipamentos.all()

    total_equipamentos = 0.0
    for equipamento in equipamentos:
        total_equipamentos += float(equipamento.custo_total)

    context = {
        'intervencao': intervencao,
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
        'equipamentos': equipamentos,
        'intervencao': intervencao,
        'total_equipamentos': total_equipamentos,
    }
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def excluir_intervencao(request, intervencao_id):
    intervencao = get_object_or_404(Intervencao, id=intervencao_id)
    intervencao.delete()
    
    return redirect('intervencoes:lista_intervencoes')