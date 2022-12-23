from django.conf import settings
from django.db import models

from nyrkes.models.base import BaseModel


class OrganizationMember(BaseModel):
    """
    An OrganizationMember is a single application user who belongs to an Organization(s).
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    organization = models.ForeignKey(
        "nyrkes.Organization",
        on_delete=models.CASCADE,
    )

    is_manager = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user}"
