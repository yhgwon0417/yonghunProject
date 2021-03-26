from django.conf.urls import url
from django.urls import  include
from rest_framework import routers

from . import InspectionSerializer, InspectionSerializer

app_name = 'inspection'
router = routers.DefaultRouter()
router.register(r'list', InspectionSerializer.InsepctionViewSet)

urlpatterns = [
    url(r'^', include(router.urls))


]
