from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'equipamentos'

router = routers.SimpleRouter()
router.register('', views.EquipamentoViewSet, basename='equipamentos')

urlpatterns = [
    path('', include(router.urls) )
]
