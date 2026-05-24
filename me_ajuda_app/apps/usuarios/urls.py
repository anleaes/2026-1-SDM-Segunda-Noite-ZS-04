from django.urls import path, include
from . import views
from rest_framework import routers

# Create your urls here.
app_name = 'usuarios'

router = routers.SimpleRouter()
router.register('', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls) )
]