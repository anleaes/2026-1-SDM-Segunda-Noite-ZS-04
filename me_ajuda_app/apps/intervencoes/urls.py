from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'intervencoes'

router = routers.SimpleRouter()
router.register('', views.IntervencaoViewSet, basename='intervencoes')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.listar_intervencoes, name='intervencoes_lista'),
    path('alocacao/', views.alocacao_equipamentos, name='alocacao_equipamentos'),
    path('alocacao/adicionar/<int:equipamento_id>/', views.add_equipamento, name='add_equipamento'),
    path('alocacao/remover/<int:equipamento_id>/', views.delete_equipamento, name='delete_equipamento'),
    path('alocacao/editar/<int:equipamento_id>/', views.edit_equipamento, name='edit_equipamento'),
    path('criar/<int:ocorrencia_id>/', views.nova_intervencao, name='nova_intervencao'),
    # path('<int:intervencao_id>/', views.ver_intervencao, name='ver_intervencao'),
    # path('<int:intervencao_id>/cancelar', views.cancelar_intervencao, name='cancelar_intervencao'),
    # path('equipamentos/', views.lista_equipamentos_intervencao, name='lista_equipamentos_intervencao'),
]
