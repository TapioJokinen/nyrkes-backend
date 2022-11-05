from typing import Any

from django.apps import apps
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.functions import Length

from menel.models import MenelManager, MenelModel

models.CharField.register_lookup(Length)


class OrganizationManager(MenelManager):
    def create(self, **kwargs: Any) -> "Organization":
        """Create Organization.

        Organization owner will also be added as member of the Organization.
        """

        org = super().create(**kwargs)
        OrganizationMember = apps.get_model("menel", "OrganizationMember")
        OrganizationMember.objects.create(user=kwargs["owner"], organization=org, invited_by=None)
        return org


class Organization(MenelModel):
    """An Organization represents a group of people.

    The members of an Organization can fulfill tasks either alone or in Squads.
    """

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
        through="menel.OrganizationMember",
        related_name="org_members",
        through_fields=("organization", "user"),
    )

    objects = OrganizationManager()

    class Meta:
        constraints = [
            models.CheckConstraint(name="org_name_min_length", check=Q(name__length__gte=2)),
        ]

    def __str__(self) -> str:
        return f"{self.name}"
