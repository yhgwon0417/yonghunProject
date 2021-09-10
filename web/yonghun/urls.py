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
# from .views import kakao_login, kakao_callback
from .views import kakao_callback, kakao_login, KakaoLogin

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

    # path('account/login/kakao/', kakao_login, name='kakao_login'),
    # path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),
    path('account/kakao/login/finish/', KakaoLogin.as_view(), name='kakao_todjango_login'),

    # path('account/login/google/callback/', google_callback, name='google_callback'),
    # path('account/google/login/finish/', GoogleLogin.as_view(), name='google_todjango_login'),

]


