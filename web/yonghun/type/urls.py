from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import TypeSerializer

app_name = 'type'
router = routers.DefaultRouter()
router.register(r'list', TypeSerializer.TypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls))


]
