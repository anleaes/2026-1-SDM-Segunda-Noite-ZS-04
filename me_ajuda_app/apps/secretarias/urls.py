from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'secretarias'

router = routers.SimpleRouter()
router.register('', views.SecretariaViewSet, basename='secretarias')

urlpatterns = [
    path('api/', include(router.urls) ),
    path('secretarias/', views.secretaria_lista, name='secretarias_lista'),
    path('nova/', views.secretaria_criar, name='secretaria_criar'),
]
