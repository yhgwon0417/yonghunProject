from django.conf.urls import url
from django.db import router
from django.urls import path, include
from rest_framework import routers

from . import CommentSerializer

app_name = 'comment'
router = routers.DefaultRouter()
router.register(r'list', CommentSerializer.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
