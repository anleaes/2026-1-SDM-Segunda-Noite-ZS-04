from django.urls import path, include
from . import views
from rest_framework import routers

# Create your urls here.
app_name = 'usuarios'

router = routers.SimpleRouter()
router.register('', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('ver-usuario/', views.usuario_perfil, name='usuario_perfil'),
    path('editar-usuario/', views.editar_perfil, name='editar_perfil'),
    # path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
]