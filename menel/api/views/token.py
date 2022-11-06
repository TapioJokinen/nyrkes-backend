from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from menel.api.serializers.token import (
    CookieTokenBlacklistSerializer,
    CookieTokenRefreshSerializer,
    CookieTokenVerifySerializer,
)


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE_KEY_REFRESH"],
                value=response.data["refresh"],
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            )
            del response.data["refresh"]

        if response.data.get("access"):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE_KEY_ACCESS"],
                value=response.data["access"],
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            )
            del response.data["access"]
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE_KEY_REFRESH"],
                value=response.data["refresh"],
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            )
            del response.data["refresh"]

        if response.data.get("access"):
            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE_KEY_ACCESS"],
                value=response.data["access"],
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            )
            del response.data["access"]
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = CookieTokenRefreshSerializer


class CookieTokenVerifyView(TokenVerifyView):
    serializer_class = CookieTokenVerifySerializer


class CookieTokenBlacklistView(TokenBlacklistView):
    serializer_class = CookieTokenBlacklistSerializer
