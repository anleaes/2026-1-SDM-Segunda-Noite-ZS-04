from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'servicos'

router = routers.SimpleRouter()
router.register('', views.ServicoViewSet, basename='servicos')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('lista/', views.servicos_lista, name='servicos_lista'),
    path('novo/', views.servico_criar, name='servico_criar'),
]
