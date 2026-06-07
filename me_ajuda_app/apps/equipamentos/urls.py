from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'equipamentos'

router = routers.SimpleRouter()
router.register('', views.EquipamentoViewSet, basename='equipamentos')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.equipamentos_lista, name='equipamentos_lista'),
    path('criar/', views.equipamento_criar, name='equipamento_criar'),
    # path('editar/<int:equipamento_id>/', views.editar_equipameto, name='editar_equipameto'),
    # path('excluir/<int:equipamento_id>/', views.excluir_equipameto, name='excluir_equipameto'),
]
