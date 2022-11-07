from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from nyrkes.api.serializers.token import (
    CookieTokenBlacklistSerializer,
    CookieTokenRefreshSerializer,
    CookieTokenVerifySerializer,
)


class CookieTokenSerializerTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.EMAIL = "foo@bar.com"
        cls.PASSWORD = "foobarz"
        User = get_user_model()
        cls.user = User.objects.create_user(email=cls.EMAIL, password=cls.PASSWORD, first_name="foo", last_name="bar")

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()

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
