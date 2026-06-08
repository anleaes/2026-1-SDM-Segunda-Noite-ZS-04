from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'equipamentos'

router = routers.SimpleRouter()
router.register('', views.EquipamentoViewSet, basename='equipamentos')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.lista_equipamentos, name='lista_equipamentos'),
    path('criar/', views.criar_equipamento, name='criar_equipamento'),
    path('editar/<int:equipamento_id>/', views.editar_equipamento, name='editar_equipamento'),
    path('excluir/<int:equipamento_id>/', views.excluir_equipamento, name='excluir_equipamento'),
]
