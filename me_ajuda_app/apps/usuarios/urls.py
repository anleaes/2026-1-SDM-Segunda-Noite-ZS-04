from django.urls import path, include
from . import views
from rest_framework import routers

# Create your urls here.
app_name = 'usuarios'

router = routers.SimpleRouter()
router.register('', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('perfil/', views.usuario_perfil, name='usuario_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('api/', include(router.urls))
]