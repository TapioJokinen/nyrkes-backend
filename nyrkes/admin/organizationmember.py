from django.contrib import admin

from nyrkes.models import OrganizationMember


class OrganizationMemberAdmin(admin.ModelAdmin):
    model = OrganizationMember

    list_display = (
        "id",
        "user",
        "organization",
    )

    ordering = ("organization",)
