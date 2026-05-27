from django.shortcuts import render


# Create your views here.
def home(request):
    template_name = 'core/home.html'
    context = {}

    if request.user.is_authenticated:
        try:
            user = request.user.usuario
            context["is_cidadao"] = hasattr(user, "cidadao")
            context["is_funcionario"] = hasattr(user, "funcionario")
        except Exception:
            context["is_cidadao"] = False
            context["is_funcionario"] = False

    return render(request, template_name, context)
