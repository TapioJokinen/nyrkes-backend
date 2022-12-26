from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from nyrkes.api.serializers.token import (
    CookieTokenBlacklistSerializer,
    CookieTokenRefreshSerializer,
    CookieTokenVerifySerializer,
)
from tests.factories import UserFactory


class CookieTokenSerializerTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user = UserFactory()

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

    def test_refresh_serializer_refresh_token_invalid(self):
        self.assertEqual(CookieTokenRefreshSerializer.refresh, None)

        request = self.factory.post("/", {}, format="json")
        request.COOKIES = {"refresh_token": "foobar"}
        test_context = {"request": request}

        serializer = CookieTokenRefreshSerializer(context=test_context)

        with self.assertRaises(TokenError):
            serializer.validate({})

    def test_refresh_serializer_no_token(self):
        request = self.factory.post("/", {}, format="json")
        request.COOKIES = {}
        test_context = {"request": request}

        serializer = CookieTokenRefreshSerializer(context=test_context)

        with self.assertRaises(InvalidToken):
            serializer.validate({})

    def test_verify_serializer_token_invalid(self):
        self.assertEqual(CookieTokenVerifySerializer.token, None)

        request = self.factory.post("/", {}, format="json")
        request.COOKIES = {"refresh_token": "foobar"}
        test_context = {"request": request}

        serializer = CookieTokenVerifySerializer(context=test_context)

        with self.assertRaises(TokenError):
            serializer.validate({})

    def test_verify_serializer_no_token(self):
        request = self.factory.post("/", {}, format="json")
        request.COOKIES = {}
        test_context = {"request": request}

        serializer = CookieTokenVerifySerializer(context=test_context)

        with self.assertRaises(InvalidToken):
            serializer.validate({})

    def test_blacklist_serializer_token_invalid(self):
        self.assertEqual(CookieTokenBlacklistSerializer.refresh, None)

        request = self.factory.post("/", {}, format="json")
        request.COOKIES = {"refresh_token": "foobar"}
        test_context = {"request": request}

        serializer = CookieTokenBlacklistSerializer(context=test_context)

        with self.assertRaises(TokenError):
            serializer.validate({})

    def test_blacklist_serializer_no_token(self):
        request = self.factory.post("/", {}, format="json")
        request.COOKIES = {}
        test_context = {"request": request}

        serializer = CookieTokenBlacklistSerializer(context=test_context)

        with self.assertRaises(InvalidToken):
            serializer.validate({})
