from django.contrib.auth import get_user_model
from django.test import TestCase

from nyrkes.models.organization import Organization
from nyrkes.models.organizationmember import OrganizationMember


class OrganizationMemberTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.User = get_user_model()
        cls.user = cls.User.objects.create_user(
            email="foo@bar.com", password="foobarz", first_name="foo", last_name="bar"
        )
        cls.org = Organization.objects.create(owner=cls.user, name="FooBarz")

    def test_string_representation(self) -> None:
        org_member = OrganizationMember.objects.get(organization=self.org, user=self.user)

        self.assertEqual(str(org_member), str(self.user))
