from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ocorrencias'

router = routers.SimpleRouter()
router.register('', views.OcorrenciaViewSet, basename='ocorrencias')

urlpatterns = [
    path('api/', include(router.urls)),
    path('painel/', views.painel_funcionario, name='painel_funcionario'),
    path('listar/', views.ocorrencias_lista, name='ocorrencias_lista'),
    path('atualizar-status/<int:ocorrencia_id>/', views.atualizar_status, name='atualizar_status'),
    path('criar/', views.ocorrencia_criar, name='ocorrencia_criar'),
    path('<int:id>/', views.visualizar_ocorrencia, name='visualizar_ocorrencia'),
    path('excluir/<int:id>/', views.ocorrencia_deletar, name='ocorrencia_deletar'),
    # path('editar/<int:id>/', views.editar_ocorrencia, name='editar_ocorrencia'),
]
