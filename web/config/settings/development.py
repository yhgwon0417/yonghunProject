from .base import *

DEBUG = True


#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blessed_test',
        'USER': 'yhgwon0417',
        'PASSWORD': 'yhgwon0417',
        'HOST': 'yeub.iptime.org',
        'PORT': '35432',
    }
}

ALLOWED_HOSTS = ["*"]
# CORS_ORIGIN_WHITELIST = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


HOST = "http://localhost:8000"