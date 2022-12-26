from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate

from nyrkes.api.views.user_organizations import UserOrganizations
from tests.factories import OrganizationFactory, UserFactory


class UserOrganizationTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = UserFactory()
        cls.org = OrganizationFactory(owner=cls.user)

    def setUp(self) -> None:
        super().setUp()
        self.factory = APIRequestFactory()
        self.view = UserOrganizations.as_view()

    def test_user_organizations(self):
        path = reverse("user_organizations")
        request = self.factory.get(
            path,
            HTTP_ACCEPT="application/json; version=1.0",
            HTTP_CONTENT_TYPE="application/json",
        )
        force_authenticate(request, self.user)
        response = self.view(request)

        correct_keys = [
            "id",
            "dateAdded",
            "dateUpdated",
            "name",
            "altName",
            "ownerId",
            "logo",
        ]

        for k in response.data[0].keys():
            self.assertIn(k, correct_keys)
            correct_keys.remove(k)

        self.assertTrue(len(correct_keys) == 0)
