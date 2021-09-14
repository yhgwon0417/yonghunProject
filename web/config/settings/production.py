from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blessed_prod',
        'USER': 'yhgwon0417',
        'PASSWORD': 'yhgwon0417',
        'HOST': 'yeub.iptime.org',
        'PORT': '35432',
    }
}

ALLOWED_HOSTS = ["yeub.iptime.org"]
CORS_ORIGIN_WHITELIST = ['http://yeub.iptime.org:8081']