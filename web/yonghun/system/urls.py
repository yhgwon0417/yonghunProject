from django.conf.urls import url
from django.urls import  include
from rest_framework import routers

from . import SystemSerializer

app_name = 'System'
router = routers.DefaultRouter()
router.register(r'list', SystemSerializer.SystemViewSet)

urlpatterns = [
    url(r'^', include(router.urls))


]
