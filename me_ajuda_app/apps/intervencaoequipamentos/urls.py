from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'intervencaoequipamentos'

router = routers.SimpleRouter()
router.register('', views.IntervencaoEquipamentoViewSet, basename='equipamentos_intervencao')

urlpatterns = [
    path('', include(router.urls) )
]