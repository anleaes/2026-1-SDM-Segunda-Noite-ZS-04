from django.shortcuts import render


# Create your views here.
def home(request):
    template_name = 'core/home.html'
    context = {}

    if request.user.is_authenticated:
        try:
            usuario = request.user.usuario
            is_cidadao = hasattr(usuario, "cidadao")
            is_funcionario = hasattr(usuario, "funcionario")
        except Exception:
            is_funcionario = False
            is_cidadao = False

    context = {
        'is_cidadao': is_cidadao,
        'is_funcionario': is_funcionario,
    }

    return render(request, template_name, context)
