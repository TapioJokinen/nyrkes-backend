from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from nyrkes.api.serializers.token import (
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
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH_MAX_AGE"],
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
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS_MAX_AGE"],
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
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH_MAX_AGE"],
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
                max_age=settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS_MAX_AGE"],
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
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception:  # pylint: disable=broad-except
            # Exception might be raised if user manually deleted refresh_token cookie.
            # We still want to return response so cookies get cleaned from the browser.
            pass

        return Response(status=status.HTTP_204_NO_CONTENT)

    def finalize_response(self, request, response, *args, **kwargs):
        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE_KEY_REFRESH"],
            value="",
            max_age=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH_MAX_AGE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        )

        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE_KEY_ACCESS"],
            value="",
            max_age=settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS_MAX_AGE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        )
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = CookieTokenBlacklistSerializer
