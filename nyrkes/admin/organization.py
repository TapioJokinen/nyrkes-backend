from django.contrib import admin

from nyrkes.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization

    list_display = (
        "id",
        "name",
        "alt_name",
        "owner",
    )

    def save_model(self, request, obj, form, change):
        if not change:
            Organization.objects.create(**form.cleaned_data)
            return None
        return super().save_model(request, obj, form, change)
