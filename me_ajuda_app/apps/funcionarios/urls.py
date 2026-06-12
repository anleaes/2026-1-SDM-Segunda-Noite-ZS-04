from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'funcionarios'

router = routers.SimpleRouter()
router.register('', views.FuncionarioViewSet, basename='funcionarios')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.lista_funcionarios, name='lista_funcionarios'),
    path('editar/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    path('excluir/<int:funcionario_id>/', views.excluir_funcionario, name='excluir_funcionario'),
]