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

from django.urls import path, include

from . import views

from .views import KakaoLogin, GoogleLogin, NaverLogin

urlpatterns = [
    path("", views.index, name='index'),
    ## Site
    path("blog/", include('yonghun.blog.urls')),

    path("company/", include('yonghun.company.urls')),
    path("schedule/", include('yonghun.schedule.urls')),
    path("inspection/", include('yonghun.inspection.urls')),
    path("system/", include('yonghun.system.urls')),
    path("type/", include('yonghun.type.urls')),
    path("contact/", include('yonghun.contact.urls')),
    path("profile/", include('yonghun.profile.urls')),

    ## 카카오
    path('account/kakao/login/finish/', KakaoLogin.as_view(), name='kakao_todjango_login'),

    ## 구글
    path('account/google/login/finish/', GoogleLogin.as_view(), name='google_todjango_login'),

    ## 네이버
    path('account/naver/login/finish/', NaverLogin.as_view(), name='naver_todjango_login'),

]
