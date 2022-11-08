from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env("SECRET_KEY", default="SET_SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

REST_FRAMEWORK["AUTH_COOKIE_SAME_SITE"] = None

SIMPLE_JWT["SIGNING_KEY"] = SECRET_KEY

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]
