from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ocorrencias'

router = routers.SimpleRouter()
router.register('', views.OcorrenciaViewSet, basename='ocorrencias')

urlpatterns = [
    path('api/', include(router.urls)),
    path('painel/', views.painel_funcionario, name='painel_funcionario'),
   # path('ocorrencia/criar', ocorrencia_form, name='ocorrencia_novo'),
    path('lista/', views.ocorrencias_lista, name='ocorrencias_lista'),
]
