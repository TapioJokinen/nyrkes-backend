from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase

from nyrkes.models.organization import Organization
from nyrkes.models.organizationmember import OrganizationMember


class OrganizationTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User = get_user_model()
        cls.user = User.objects.create_user(email="foo@bar.com", password="foobarz", first_name="foo", last_name="bar")

    def test_max_lengths(self) -> None:
        name_length = Organization._meta.get_field("name").max_length  # pylint: disable=protected-access, no-member

        self.assertEqual(name_length, 100)

    def test_string_representation(self) -> None:
        org = Organization.objects.create(owner=self.user, name="FooBarz")

        self.assertEqual(str(org), "FooBarz")

    def test_constraint_org_name_min_length(self) -> None:
        with self.assertRaises(IntegrityError):
            Organization.objects.create(owner=self.user, name="A")

    def test_owner_is_member_of_org(self) -> None:
        org = Organization.objects.create(owner=self.user, name="Bazooka")

        try:
            OrganizationMember.objects.get(user=self.user, organization=org)
        except OrganizationMember.DoesNotExist:
            assert False
        else:
            assert True
