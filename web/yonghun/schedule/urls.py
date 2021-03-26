from django.conf.urls import url
from django.urls import  include
from rest_framework import routers

from . import ScheduleSerializer

app_name = 'schedule'
router = routers.DefaultRouter()
router.register(r'list', ScheduleSerializer.ScheduleViewSet)

urlpatterns = [
    url(r'^', include(router.urls))


]
