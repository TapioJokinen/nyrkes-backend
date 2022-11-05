from django.conf import settings
from django.db import models

from menel.models import MenelModel


class OrganizationMember(MenelModel):
    """
    An OrganizationMember is a single application user who belongs to an Organization.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    organization = models.ForeignKey(
        "menel.Organization",
        on_delete=models.CASCADE,
    )

    invited_by = models.ForeignKey(
        "menel.OrganizationMember",
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(name="user_organization_unique", fields=["user", "organization"]),
        ]

    def __str__(self) -> str:
        return f"{self.user}"
