from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'intervencoes'

router = routers.SimpleRouter()
router.register('', views.IntervencaoViewSet, basename='intervencoes')

urlpatterns = [
    path('', include(router.urls) )
]
