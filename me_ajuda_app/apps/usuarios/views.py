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

def registrar(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)

        if user_form.is_valid() and usuario_form.is_valid():
            f_user = user_form.save(commit=False)
            f_user.set_password(f_user.password)
            f_user.username = usuario_form.cleaned_data.get('cpf')
            f_user.save()

            f_usuario = usuario_form.save(commit=False)
            f_usuario.user = f_user
            f_usuario.save()

            messages.success(request, 'Conta criada com sucesso!')
            return redirect('usuarios:login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        user_form = UserForm()
        usuario_form = UsuarioForm()

    context = {
        'user_form': user_form,
        'usuario_form': usuario_form,
    }
    
    return render(request, 'registrar.html', context)

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
    return render(request, 'usuario_perfil.html', context)

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
                
            return redirect('usuario_perfil')
            
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
    
    return render(request, 'editar_perfil.html', context)