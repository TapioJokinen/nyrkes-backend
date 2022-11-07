from django.contrib.auth import get_user_model
from django.test import TestCase

from nyrkes.models.user import User
from nyrkes.utils.constants import Errors


class UserManagerTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.User = get_user_model()

    def test_create_user(self) -> None:

        user = self.User.objects.create_user(email="foo@bar.com", password="foobar", first_name="foo", last_name="bar")
        self.assertEqual(user.email, "foo@bar.com")
        self.assertEqual(user.first_name, "foo")
        self.assertEqual(user.last_name, "bar")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaisesMessage(ValueError, str(Errors.REQUIRED_FIELD_EMAIL)):
            self.User.objects.create_user(email=None, password="foobar", first_name="foo", last_name="bar")

        with self.assertRaisesMessage(ValueError, str(Errors.REQUIRED_FIELD_FIRST_NAME)):
            self.User.objects.create_user(email="foo@bar.com", password="foobar", last_name="bar")

        with self.assertRaisesMessage(ValueError, str(Errors.REQUIRED_FIELD_LAST_NAME)):
            self.User.objects.create_user(email="foo@bar.com", password="foobar", first_name="foo")

    def test_create_superuser(self) -> None:

        user = self.User.objects.create_superuser(
            email="foo@bar.com", password="foobar", first_name="foo", last_name="bar"
        )
        self.assertEqual(user.email, "foo@bar.com")
        self.assertEqual(user.first_name, "foo")
        self.assertEqual(user.last_name, "bar")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaisesMessage(ValueError, str(Errors.REQUIRED_FIELD_EMAIL)):
            self.User.objects.create_superuser(email=None, password="foobar", first_name="foo", last_name="bar")

        with self.assertRaisesMessage(ValueError, str(Errors.REQUIRED_FIELD_FIRST_NAME)):
            self.User.objects.create_superuser(email="foo@bar.com", password="foobar", last_name="bar")

        with self.assertRaisesMessage(ValueError, str(Errors.REQUIRED_FIELD_LAST_NAME)):
            self.User.objects.create_superuser(email="foo@bar.com", password="foobar", first_name="foo")

        with self.assertRaisesMessage(ValueError, str(Errors.SUPERUSER_NOT_STAFF)):
            self.User.objects.create_superuser(
                email="foo@bar.com", password="foobar", first_name="foo", last_name="bar", is_staff=False
            )

        with self.assertRaisesMessage(ValueError, str(Errors.SUPERUSER_NOT_SUPERUSER)):
            self.User.objects.create_superuser(
                email="foo@bar.com", password="foobar", first_name="foo", last_name="bar", is_superuser=False
            )


class UserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.User = get_user_model()

    def test_user_model(self) -> None:
        self.assertTrue(self.User == User)

    def test_username_field(self) -> None:
        self.assertEqual(self.User.USERNAME_FIELD, "email")

    def test_required_fields(self) -> None:
        self.assertEqual(self.User.REQUIRED_FIELDS, ["first_name", "last_name"])

    def test_string_representation(self) -> None:
        user = self.User.objects.create_user(email="foo@bar.com", password="foobar", first_name="foo", last_name="bar")

        self.assertEqual(str(user), "foo@bar.com")
