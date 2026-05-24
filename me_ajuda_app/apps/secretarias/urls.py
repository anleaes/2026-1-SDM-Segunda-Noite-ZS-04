from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'secretarias'

router = routers.SimpleRouter()
router.register('', views.SecretariaViewSet, basename='secretarias')

urlpatterns = [
    path('', include(router.urls) )
]