from django.apps import apps
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.functions import Length

from nyrkes.models.base import BaseManager, BaseModel
from nyrkes.tasks import resize_img

models.CharField.register_lookup(Length)


class OrganizationManager(BaseManager):
    def create(self, **kwargs):
        """Create Organization.

        The Organization owner will also be added as member of the Organization.
        """
        org = super().create(**kwargs)
        OrganizationMember = apps.get_model("nyrkes", "OrganizationMember")
        OrganizationMember.objects.create(user=kwargs["owner"], organization=org)
        return org

    def get_user_orgs(self, user_id):
        return self.filter(members__in=[user_id])


class Organization(BaseModel):
    """An Organization represents a group of people."""

    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
    )
    alt_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="nyrkes.OrganizationMember",
        related_name="org_members",
        through_fields=("organization", "user"),
    )

    logo = models.ImageField(upload_to="logos", default=None)

    objects = OrganizationManager()

    class Meta:
        constraints = [
            models.CheckConstraint(name="org_name_min_length", check=Q(name__length__gte=2)),
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        # We get database connection error if celery-task is run during testing
        # therefore disable celery-task while testing.
        if not settings.TESTING:  # pragma: no cover
            resize_img.delay(self.logo.path)  # pylint: disable=no-member
