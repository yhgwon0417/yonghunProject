"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
import json
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7sehy8po%1$xhy-5t(%2c@p!ou=wf0ww1vgzi@@q$tv&_uc!xo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## Custom
    'yonghun',
    'django_filters',
    'debug_toolbar',

    # django-rest-auth
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_auth',
    'rest_auth.registration',

    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.sites',
    # provider
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
]

# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = False

# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_VERIFICATION = "none"

REST_USE_JWT = True
ACCOUNT_LOGOUT_ON_GET = True

SITE_ID = 2

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',## 설정하면, CSRf 필요없음
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',## 설정하면, Refresh 가능
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',

    'PAGE_SIZE': 10,

}

JWT_AUTH = {'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
            'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
            'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
            'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
            'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
            'JWT_SECRET_KEY': SECRET_KEY, 'JWT_GET_USER_SECRET_KEY': None, 'JWT_PUBLIC_KEY': None,
            'JWT_PRIVATE_KEY': None, 'JWT_ALGORITHM': 'HS256', 'JWT_VERIFY': True, 'JWT_VERIFY_EXPIRATION': True,
            'JWT_LEEWAY': 0, 'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1), 'JWT_AUDIENCE': None,
            'JWT_ISSUER': None,
            'JWT_ALLOW_REFRESH': True, 'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=1),
            'JWT_AUTH_HEADER_PREFIX': 'JWT', 'JWT_AUTH_COOKIE': None, }
REST_USE_JWT = True

# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',
#
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

SECRET_BASE_FILE = './secrets.json'
secrets = json.loads(open(SECRET_BASE_FILE).read())
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

AUTH_USER_MODEL = 'yonghun.User'

CORS_ORIGIN_WHITELIST = ['http://localhost:8081', 'http://yonghun.net:8081', 'http://127.0.0.1:8081']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEBUG = True

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blessed',
        'USER': 'yhgwon0417',
        'PASSWORD': 'yhgwon0417',
        'HOST': 'yeub.iptime.org',
        'PORT': '35432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

LOGIN_REDIRECT_URL = '/'
