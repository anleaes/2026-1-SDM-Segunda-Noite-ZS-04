from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'secretarias'

router = routers.SimpleRouter()
router.register('', views.SecretariaViewSet, basename='secretarias')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.lista_secretarias, name='lista_secretarias'),
    path('criar/', views.criar_secretaria, name='criar_secretaria'),
    path('editar/<int:secretaria_id>/', views.editar_secretaria, name='editar_secretaria'),
    path('excluir/<int:secretaria_id>/', views.excluir_secretaria, name='excluir_secretaria'),
]
