from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import CompanySerializer

app_name = 'company'
router = routers.DefaultRouter()
router.register(r'list', CompanySerializer.CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls))


]
