from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from nyrkes.authentication import CookieAuthentication


def mock_get_validated_token(self, token):  # pylint: disable=unused-argument
    return "foobar"


def mock_get_user(self, token):  # pylint: disable=unused-argument
    return "Bob"


def mock_get_raw_token(self, header):  # pylint: disable=unused-argument
    return "foobar"


def mock_get_raw_token_none(self, header):  # pylint: disable=unused-argument
    return None


class CookieAuthenticationTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.factory = APIRequestFactory()

    def test_header_is_none(self):
        request = self.factory.post("/", {}, format="json")
        request.COOKIES[settings.SIMPLE_JWT["AUTH_COOKIE_KEY_ACCESS"]] = "foobar"

        with patch.object(CookieAuthentication, "get_validated_token", mock_get_validated_token):
            with patch.object(CookieAuthentication, "get_user", mock_get_user):
                result = CookieAuthentication().authenticate(request)

        self.assertEqual(result, ("Bob", "foobar"))

    def test_header_is_not_none(self):
        settings.DEBUG = True
        request = self.factory.post("/", {}, format="json", HTTP_AUTHORIZATION={"Authorization": "bar"})

        with patch.object(CookieAuthentication, "get_raw_token", mock_get_raw_token):
            with patch.object(CookieAuthentication, "get_validated_token", mock_get_validated_token):
                with patch.object(CookieAuthentication, "get_user", mock_get_user):
                    result = CookieAuthentication().authenticate(request)

        self.assertEqual(result, ("Bob", "foobar"))

    def test_header_is_not_none_and_raw_token_is_none(self):
        settings.DEBUG = True
        request = self.factory.post("/", {}, format="json", HTTP_AUTHORIZATION={"Authorization": "bar"})

        with patch.object(CookieAuthentication, "get_raw_token", mock_get_raw_token_none):
            with patch.object(CookieAuthentication, "get_validated_token", mock_get_validated_token):
                with patch.object(CookieAuthentication, "get_user", mock_get_user):
                    result = CookieAuthentication().authenticate(request)

        self.assertEqual(result, None)
