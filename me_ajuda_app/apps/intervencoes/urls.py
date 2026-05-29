from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'intervencoes'

router = routers.SimpleRouter()
router.register('', views.IntervencaoViewSet, basename='intervencoes')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('lista/', views.listar_intervencoes, name='intervencoes_lista'),
    path('nova/', views.nova_intervencao, name='nova_intervencao'),
    path('alocacao/', views.alocacao_equipamentos, name='alocacao_equipamentos'),
]
