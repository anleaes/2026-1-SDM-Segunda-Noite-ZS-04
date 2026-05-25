from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'protocolos'

router = routers.SimpleRouter()
router.register('', views.ProtocoloViewSet, basename='protocolos')

urlpatterns = [
    path('', include(router.urls) )
]