from django.conf.urls import url
from django.db import router
from django.urls import path, include
from rest_framework import routers

from . import views, BlogSerializer

app_name = 'blog'
router = routers.DefaultRouter()
router.register(r'list', BlogSerializer.BlogViewSet)

urlpatterns = [
    # path('', views.BlogListView.aress_view(), name='index'),
    # path('list', views.BlogListView.as_view(), name='list'),
    # path("create/", views.BlogCreateView.as_view(), name='create'),
    # path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    # path("<int:pk>/update/", views.BlogUpdateView.as_view(), name='update'),
    # path("<int:pk>/delete/", views.BlogDeleteView.as_view(), name='delete'),
    url(r'^', include(router.urls))
    # path("<int:blog_pk>/comment/create", views.BlogCommentCreateView.as_view(), name='comment_create'),



    # url(r'^api/', include(router.urls))
]
