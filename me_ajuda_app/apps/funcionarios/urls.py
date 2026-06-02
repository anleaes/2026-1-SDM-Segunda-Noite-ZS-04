from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'funcionarios'

router = routers.SimpleRouter()
router.register('', views.FuncionarioViewSet, basename='funcionarios')

urlpatterns = [
    path('api/', include(router.urls) )
]