"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views
from .blog import BlogSerializer
from .comment import CommentSerializer
from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI, ProfileUpdateAPI

urlpatterns = [
    path("", views.index, name='index'),
    path("hello/", HelloAPI),

    path("profile/", include('yonghun.profile.urls')),
    path("blog/", include('yonghun.blog.urls')),
    # path("blog/comment/", include('yonghun.comment.urls')),
    path("contact/", include('yonghun.contact.urls')),

    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path("auth/profile/<int:user_pk>/update/", ProfileUpdateAPI.as_view()),

]
