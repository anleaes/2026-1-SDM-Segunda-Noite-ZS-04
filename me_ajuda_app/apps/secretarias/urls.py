from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'secretarias'

router = routers.SimpleRouter()
router.register('', views.SecretariaViewSet, basename='secretarias')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('listar/', views.secretaria_lista, name='secretaria_lista'),
    path('criar/', views.secretaria_criar, name='secretaria_criar'),
    path('editar/<int:id_secretaria>/', views.editar_secretaria, name='editar_secretaria'),
    path('excluir/<int:id_secretaria>/', views.excluir_secretaria, name='excluir_secretaria'),
]
