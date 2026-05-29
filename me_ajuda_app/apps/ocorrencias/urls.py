from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ocorrencias'

router = routers.SimpleRouter()
router.register('', views.OcorrenciaViewSet, basename='ocorrencias')

urlpatterns = [
    path('api/', include(router.urls)),
    path('painel/', views.painel_funcionario, name='painel_funcionario'),
    path('criar/', views.ocorrencia_criar, name='ocorrencia_criar'),
    path('lista/', views.ocorrencias_lista, name='ocorrencias_lista'),
    path('visualizar/<int:id>/', views.visualizar_ocorrencia, name='visualizar_ocorrencia'),
    path('atualizar-status/<int:ocorrencia_id>/', views.atualizar_status, name='atualizar_status'),
    path('deletar/<int:id>/', views.ocorrencia_deletar, name='ocorrencia_deletar'),
]
