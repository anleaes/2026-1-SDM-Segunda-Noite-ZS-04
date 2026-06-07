from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'servicos'

router = routers.SimpleRouter()
router.register('', views.ServicoViewSet, basename='servicos')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.servicos_lista, name='servicos_lista'),
    path('criar/', views.servico_criar, name='servico_criar'),
    path('editar/<int:id_servico>/', views.editar_servico, name='editar_servico'),
    path('excluir/<int:id_servico>/', views.excluir_servico, name='excluir_servico'),
]
