from django.test import TestCase

from nyrkes.models.organization import Organization
from nyrkes.models.organizationmember import OrganizationMember
from tests.factories import UserFactory


class OrganizationMemberTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user = UserFactory()
        cls.org = Organization.objects.create(owner=cls.user, name="FooBarz")

    def test_string_representation(self) -> None:
        org_member = OrganizationMember.objects.get(organization=self.org, user=self.user)

        self.assertEqual(str(org_member), str(self.user))
