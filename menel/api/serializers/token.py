from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import (
    TokenBlacklistSerializer,
    TokenRefreshSerializer,
    TokenVerifySerializer,
)


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["refresh"]:
            return super().validate(attrs)
        raise InvalidToken("No valid token found in cookie 'refresh_token'")


class CookieTokenVerifySerializer(TokenVerifySerializer):
    token = None

    def validate(self, attrs):
        attrs["token"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["token"]:
            return super().validate(attrs)
        raise InvalidToken("No valid token found in cookie 'refresh_token'")


class CookieTokenBlacklistSerializer(TokenBlacklistSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["refresh"]:
            return super().validate(attrs)
        raise InvalidToken("No valid token found in cookie 'refresh_token'")
