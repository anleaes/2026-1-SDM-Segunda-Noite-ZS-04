from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'equipamentos'

router = routers.SimpleRouter()
router.register('', views.EquipamentoViewSet, basename='equipamentos')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('lista/', views.equipamentos_lista, name='equipamentos_lista'),
    path('novo/', views.equipamento_criar, name='equipamento_criar'),
]
