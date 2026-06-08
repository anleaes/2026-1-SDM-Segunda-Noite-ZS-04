from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'intervencoes'

router = routers.SimpleRouter()
router.register('', views.IntervencaoViewSet, basename='intervencoes')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.lista_intervencoes, name='lista_intervencoes'),
    path('alocacao/', views.alocacao_equipamentos, name='alocacao_equipamentos'),
    path('alocacao/adicionar/<int:equipamento_id>/', views.adicionar_alocacao, name='adicionar_alocacao'),
    path('alocacao/remover/<int:equipamento_id>/', views.excluir_alocacao, name='excluir_alocacao'),
    path('alocacao/editar/<int:equipamento_id>/', views.editar_alocacao, name='editar_alocacao'),
    path('criar/<int:ocorrencia_id>/', views.criar_intervencao, name='criar_intervencao'),
    path('equipamentos/', views.lista_equipamentos_intervencao, name='lista_equipamentos_intervencao'),
    path('<int:intervencao_id>/', views.ver_intervencao, name='ver_intervencao'),
    path('editar/<int:intervencao_id>/', views.editar_intervencao, name='editar_intervencao'),
    path('excluir/<int:intervencao_id>/', views.excluir_intervencao, name='excluir_intervencao'),
]
