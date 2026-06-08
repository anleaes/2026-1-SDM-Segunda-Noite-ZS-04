from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cidadaos'

router = routers.SimpleRouter()
router.register('', views.CidadaoViewSet, basename='cidadaos')

urlpatterns = [
    path('api/', include(router.urls) ),
]