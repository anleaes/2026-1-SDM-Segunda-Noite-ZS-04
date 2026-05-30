from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'intervencoes'

router = routers.SimpleRouter()
router.register('', views.IntervencaoViewSet, basename='intervencoes')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('lista/', views.listar_intervencoes, name='intervencoes_lista'),
    path('nova/<int:ocorrencia_id>/', views.nova_intervencao, name='nova_intervencao'),
    path('alocacao/', views.alocacao_equipamentos, name='alocacao_equipamentos'),
    path('adicionar/<int:equipamento_id>/', views.add_equipamento, name='add_equipamento'),
    path('remover/<int:equipamento_id>/', views.delete_equipamento, name='delete_equipamento'),
    path('editar/<int:equipamento_id>/', views.edit_equipamento, name='edit_equipamento'),
]
