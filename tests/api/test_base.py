from django.test import TestCase
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIRequestFactory

from nyrkes.api.base import BaseAPIView
from nyrkes.api.exceptions import APINotImplemented


class BaseAPIViewTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.factory = APIRequestFactory()

    def test_permission_classes(self):
        self.assertEqual(BaseAPIView.permission_classes, [IsAuthenticated])

    def test_get(self):
        request = self.factory.get("/")

        with self.assertRaises(APINotImplemented):
            BaseAPIView().get(request)

    def test_post(self):
        request = self.factory.post("/", {}, format="json")

        with self.assertRaises(APINotImplemented):
            BaseAPIView().post(request)

    def test_put(self):
        request = self.factory.put("/", {}, format="json")

        with self.assertRaises(APINotImplemented):
            BaseAPIView().put(request)

    def test_patch(self):
        request = self.factory.get("/", {}, format="json")

        with self.assertRaises(APINotImplemented):
            BaseAPIView().patch(request)

    def test_delete(self):
        request = self.factory.get("/")

        with self.assertRaises(APINotImplemented):
            BaseAPIView().delete(request)
