from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ocorrencias'

router = routers.SimpleRouter()
router.register('', views.OcorrenciaViewSet, basename='ocorrencias')

urlpatterns = [
    path('api/', include(router.urls)),
    path('painel/', views.painel_ocorrencias, name='painel_ocorrencias'),
    path('listar/', views.lista_ocorrencias, name='lista_ocorrencias'),
    path('atualizar-status/<int:ocorrencia_id>/', views.atualizar_status_ocorrencia, name='atualizar_status_ocorrencia'),
    path('criar/', views.criar_ocorrencia, name='criar_ocorrencia'),
    path('<int:ocorrencia_id>/', views.ver_ocorrencia, name='ver_ocorrencia'),
    path('excluir/<int:ocorrencia_id>/', views.excluir_ocorrencia, name='excluir_ocorrencia'),
    path('editar/<int:ocorrencia_id>/', views.editar_ocorrencia, name='editar_ocorrencia'),
]
