from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from me_ajuda_app.apps.usuarios.forms import UsuarioForm
from .models import Usuario
from rest_framework import viewsets
from .serializer import UsuarioSerializer

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
            f_user.username = usuario_form.get('cpf')
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