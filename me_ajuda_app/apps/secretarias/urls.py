from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'secretarias'

router = routers.SimpleRouter()
router.register('', views.SecretariaViewSet, basename='secretarias')

urlpatterns = [
    path('Api/', include(router.urls) ),
    path('secretarias/', views.secretaria_lista, name='secretarias_lista'),
]
