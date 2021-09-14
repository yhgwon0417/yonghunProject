from django.conf import settings
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.google import views as google_view
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
BASE_URL = 'http://yeub.iptime.org:8000/'
# BASE_URL = HOST +"/"
KAKAO_CALLBACK_URI = BASE_URL + 'yonghun/account/login/kakao/callback'
GOOGLE_CALLBACK_URI = BASE_URL + 'yonghun/account/login/google/callback/'


class KaKaoException(Exception):
    pass


def kakao_login(request):
    rest_api_key = KAKAO_REST_API_KEY
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )


def kakao_callback(request):
    try:
        rest_api_key = KAKAO_REST_API_KEY
        redirect_uri = KAKAO_CALLBACK_URI
        code = request.GET.get("code")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
        token_request_json = token_request.json()
        error = token_request_json.get("error")
        if error is not None:
            raise KaKaoException()
        access_token = token_request_json.get("access_token")
        # profile_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"})
        # profile_json = profile_request.json()
        # kakao_account = profile_json.get('kakao_account')
        # profile = kakao_account.get("profile")
        # nickname = profile.get("nickna
        # me")
        data = {'access_token': access_token, 'code': code}


        accept = requests.post(
            "http://yeub.iptime.org:8000/yonghun/account/kakao/login/finish/", data=data
        )

        # return redirect("http://127.0.0.1:8000/" + str(accept))
        accept_json = accept.json()
        error = accept_json.get("error")
        if error is not None:
            raise KaKaoException()
        return JsonResponse(accept_json)
    except KaKaoException:
        return redirect('/error')


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI


