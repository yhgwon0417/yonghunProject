from json.decoder import JSONDecodeError

from django.conf import settings
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.naver import views as naver_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from django.http import JsonResponse

import requests
from django.shortcuts import render, redirect
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


def index(request):
    return render(request, 'index.html')


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


KAKAO_REST_API_KEY = "fcdb4932bf507a42c8be3ec4d0633ded"
SECRET_KEY = "399851"
BASE_URL = 'http://localhost:8000/'
# BASE_URL = HOST +"/"
KAKAO_CALLBACK_URI = BASE_URL + 'yonghun/account/login/kakao/callback'
GOOGLE_CALLBACK_URI = BASE_URL + 'yonghun/account/login/google/callback/'
NAVER_CALLBACK_URI = BASE_URL + 'yonghun/account/login/naver/callback/'


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


class NaverLogin(SocialLoginView):
    adapter_class = naver_view.NaverOAuth2Adapter
    callback_url = NAVER_CALLBACK_URI
    client_class = OAuth2Client
