from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usuario
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, UserForm
from cidadaos.forms import CidadaoForm
from funcionarios.forms import FuncionarioForm


# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 

def registrar_usuario(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')
        
        user_form = UserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        
        if tipo_usuario == 'cidadao':
            cidadao_form = CidadaoForm(request.POST)
            funcionario_form = FuncionarioForm()
            tipo_form_valido = cidadao_form.is_valid()
        else:
            cidadao_form = CidadaoForm()
            funcionario_form = FuncionarioForm(request.POST)
            tipo_form_valido = funcionario_form.is_valid()

        if user_form.is_valid() and usuario_form.is_valid() and tipo_form_valido:
            
            f_user = user_form.save(commit=False)
            f_user.set_password(f_user.password)
            f_user.username = usuario_form.cleaned_data.get('cpf')
            f_user.save()

            if tipo_usuario == 'cidadao':
                f_cidadao = cidadao_form.save(commit=False)
                f_cidadao.user = f_user 
                
                for campo, valor in usuario_form.cleaned_data.items():
                    setattr(f_cidadao, campo, valor)

                f_cidadao.save()
            else:
                f_funcionario = funcionario_form.save(commit=False)
                f_funcionario.user = f_user

                for campo, valor in usuario_form.cleaned_data.items():
                    setattr(f_funcionario, campo, valor)

                f_funcionario.save()
                funcionario_form.save_m2m() 

            messages.success(request, 'Conta criada com sucesso!')
            return redirect('usuarios:login_usuario')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            
    else:
        user_form = UserForm()
        usuario_form = UsuarioForm()
        cidadao_form = CidadaoForm()
        funcionario_form = FuncionarioForm()

    context = {
        'user_form': user_form,
        'usuario_form': usuario_form,
        'cidadao_form': cidadao_form,
        'funcionario_form': funcionario_form,
    }
    
    return render(request, 'usuarios/registrar_usuario.html', context)

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('usuarios:usuario_perfil')

    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        user = authenticate(request, username=cpf, password=senha)

        if user is not None:
            login(request, user)
            return redirect('usuarios:usuario_perfil')
        else:
            messages.error(request, 'CPF ou senha incorretos.')

    return render(request, 'usuarios/login_usuario.html')

@login_required(login_url='/usuarios/login/')
def logout_usuario(request):
    logout(request)
    return redirect('usuarios:login_usuario')

#criação de perfil do usuario
@login_required(login_url='/usuarios/login/')
def usuario_perfil(request):   

    try:
        usuario = request.user.usuario
    except:
        usuario = None

    context = {
        'is_cidadao': hasattr(usuario, 'cidadao'),
        'is_funcionario': hasattr(usuario, 'funcionario'),
        'usuario': usuario,
    }
    return render(request, 'usuarios/ver_usuario.html', context)

@login_required(login_url='/usuarios/login/')
def editar_perfil(request):
    usuario = request.user.usuario
    is_cidadao = hasattr(usuario, 'cidadao')
    is_funcionario = hasattr(usuario, 'funcionario')

    if is_cidadao:
        perfil = usuario.cidadao
        PerfilForm = CidadaoForm
    elif is_funcionario:
        perfil = usuario.funcionario
        PerfilForm = FuncionarioForm
    else:
        perfil = None
        PerfilForm = None

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        if PerfilForm:
            perfil_form = PerfilForm(request.POST, instance=perfil)
        else:
            perfil_form = None

        if usuario_form.is_valid() and (not perfil_form or perfil_form.is_valid()):
            usuario_form.save()
            if perfil_form:
                perfil_form.save()
                
            return redirect('usuarios:usuario_perfil')
            
    else:
        usuario_form = UsuarioForm(instance=usuario)
        if PerfilForm:
            perfil_form = PerfilForm(instance=perfil)
        else:
            perfil_form = None

    context = {
        'usuario_form': usuario_form,
        'perfil_form': perfil_form,
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
    }
    
    return render(request, 'usuarios/editar_usuario.html', context)

@login_required(login_url='/usuarios/login/')
def alterar_senha(request):
    template_name = 'usuarios/alterar_senha_usuario.html'
    context = {}

    if request.method == 'POST':
        form = UserForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            return redirect('usuarios:login_usuario')
        
    form = UserForm(user=request.user)

    context['form'] = form

    return render(request, template_name, context)