from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cidadaos'

router = routers.SimpleRouter()
router.register('', views.CidadaoViewSet, basename='cidadaos')

urlpatterns = [
    path('api/', include(router.urls) ),
    # path('listar/', views.lista_cidadaos, name='lista_cidadaos'),
    # path('editar/<int:cidadao_id>/', views.editar_cidadao, name='editar_cidadao'),
    # path('excluir/<int:cidadao_id>/', views.excluir_cidadao, name='excluir_cidadao'),
]