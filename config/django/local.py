from .base import *
from .base import env

DEBUG = True

INSTALLED_APPS += [
    "django.contrib.admin",
    "django.contrib.messages",
]

MIDDLEWARE += [
    "django.contrib.messages.middleware.MessageMiddleware",
]

SECRET_KEY = env("SECRET_KEY", default="SET_SECRET_KEY")

REST_FRAMEWORK["AUTH_COOKIE_SAME_SITE"] = None

SIMPLE_JWT["SIGNING_KEY"] = SECRET_KEY

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

CORS_ALLOW_CREDENTIALS = True
