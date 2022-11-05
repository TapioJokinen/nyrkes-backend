from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from menel.models import MenelModel
from menel.utils.constants import Errors


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        first_name = extra_fields.get("first_name", None)
        last_name = extra_fields.get("last_name", None)

        if not email:
            raise ValueError(Errors.REQUIRED_FIELD_EMAIL)
        if not first_name:
            raise ValueError(Errors.REQUIRED_FIELD_FIRST_NAME)
        if not last_name:
            raise ValueError(Errors.REQUIRED_FIELD_LAST_NAME)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        first_name = extra_fields.get("first_name", None)
        last_name = extra_fields.get("last_name", None)

        if not email:
            raise ValueError(Errors.REQUIRED_FIELD_EMAIL)
        if not first_name:
            raise ValueError(Errors.REQUIRED_FIELD_FIRST_NAME)
        if not last_name:
            raise ValueError(Errors.REQUIRED_FIELD_LAST_NAME)

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(Errors.SUPERUSER_NOT_STAFF)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(Errors.SUPERUSER_NOT_SUPERUSER)

        return self.create_user(email, password, **extra_fields)


class User(MenelModel, AbstractBaseUser, PermissionsMixin):
    """Models a single application user."""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=35, blank=False, null=False, db_index=True)
    last_name = models.CharField(max_length=35, blank=False, null=False, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_active = models.DateTimeField(auto_now=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.email}"
