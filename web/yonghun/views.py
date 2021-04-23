import urllib
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
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


def kakao_login(request):
    app_rest_api_key = 'fcdb4932bf507a42c8be3ec4d0633ded'
    redirect_uri = "http://127.0.0.1:8000/yonghun/account/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


# access token 요청
class KakaoException(Exception):
    pass


# access token 요청 함수
def kakao_callback(request):
    try:
        app_rest_api_key = 'fcdb4932bf507a42c8be3ec4d0633ded'
        redirect_uri = "http://127.0.0.1:8000/yonghun/account/login/kakao/callback"
        user_token = request.GET.get("code")

        # post request
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        error = token_response_json.get("error", None)

        # if there is an error from token_request
        if error is not None:
            raise KakaoException()
        access_token = token_response_json.get("access_token")

        # post request
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        # parsing profile json
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email", None)
        if email is None:
            raise KakaoException()  # 이메일은 필수제공 항목이 아니므로 수정 필요 (비즈니스 채널을 연결하면 검수 신청 후 필수 변환 가능)
        profile = kakao_account.get("profile")
        nickname = profile.get("nickname")
        # profile_image = profile.get("thumbnail_image_url")  # 사이즈 'thumbnail_image_url' < 'profile_image_url'
        # print('image', profile_image)

        try:
            user_in_db = User.objects.get(email=email)
            # kakao계정 email이 서비스에 이미 따로 가입된 email 과 충돌한다면
            if user_in_db.user_type != 'kakao':
                raise KakaoException()
            # 이미 kakao로 가입된 유저라면
            else:
                # 서비스에 rest-auth 로그인
                data = {'code': user_token, 'access_token': access_token}
                accept = requests.post(
                    f"http://127.0.0.1:8000/account/login/kakao/todjango", data=data
                )
                accept_json = accept.json()
                accept_jwt = accept_json.get("token")

                # 프로필 정보 업데이트
                User.objects.filter(email=email).update(username=nickname,
                                                        email=email,
                                                        # user_type='kakao',
                                                        # profile_image=profile_image,
                                                        is_active=True
                                                        )

        except User.DoesNotExist:
            # 서비스에 rest-auth 로그인
            data = {'code': user_token, 'access_token': access_token}
            accept = requests.post(
                f"http://127.0.0.1:8000/yonghun/account/login/kakao/todjango", data=data
            )
            accept_json = accept.json()
            accept_jwt = accept_json.get("token")

            User.objects.filter(email=email).update(username=nickname,
                                                    email=email,
                                                    # user_type='kakao',
                                                    # profile_image=profile_image,
                                                    is_active=True
                                                    )
        return redirect("http://127.0.0.1:8000/")  # 메인 페이지

    except KakaoException:
        return redirect("http://127.0.0.1:8000/yonghun/account/login")


class KakaoToDjangoLogin(SocialLoginView):
    adapter_class = kakao_views.KakaoOAuth2Adapter
    client_class = OAuth2Client
