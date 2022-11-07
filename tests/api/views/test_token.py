from http.cookies import SimpleCookie

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory

from nyrkes.api.views.token import CookieTokenObtainPairView, CookieTokenRefreshView


class CookieTokenViewTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.EMAIL = "foo@bar.com"
        cls.PASSWORD = "foobarz"
        User = get_user_model()
        cls.user = User.objects.create_user(email=cls.EMAIL, password=cls.PASSWORD, first_name="foo", last_name="bar")

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.response = HttpResponse()
        self.response.data = {"refresh": "foobar", "access": "barfoo"}
        self.response.COOKIE = {}

    def test_obtain_pair_view_finalize_response(self):
        path = reverse("token_obtain_pair")
        request = self.factory.post(path, {"email": self.EMAIL, "password": self.PASSWORD}, format="json")
        view = CookieTokenObtainPairView()
        view.headers = {}

        response = view.finalize_response(request, self.response)

        self.assertIsInstance(response.cookies, SimpleCookie)
        self.assertEqual(response.cookies["refresh_token"]["max-age"], settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"])
        self.assertEqual(response.cookies["refresh_token"]["samesite"], settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"])
        self.assertEqual(response.cookies["refresh_token"]["httponly"], settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"])

        # Jsut for coverage
        self.response.data = {}
        response = view.finalize_response(request, self.response)

    def test_refresh_finalize_response(self):
        path = reverse("token_refresh")
        request = self.factory.post(path, {}, format="json")
        view = CookieTokenRefreshView()
        view.headers = {}

        response = view.finalize_response(request, self.response)

        self.assertIsInstance(response.cookies, SimpleCookie)
        self.assertEqual(response.cookies["refresh_token"]["max-age"], settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"])
        self.assertEqual(response.cookies["refresh_token"]["samesite"], settings.SIMPLE_JWT["AUTH_COOKIE_SAME_SITE"])
        self.assertEqual(response.cookies["refresh_token"]["httponly"], settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"])

        # Jsut for coverage
        self.response.data = {}
        response = view.finalize_response(request, self.response)
