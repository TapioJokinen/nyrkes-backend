from django.contrib.auth import admin

from nyrkes.forms.user import UserChangeForm, UserCreationForm
from nyrkes.models import User


class UserAdmin(admin.UserAdmin):
    model = User

    add_form = UserCreationForm

    form = UserChangeForm

    search_fields = ("id", "email", "first_name", "last_name", "phone_number")

    ordering = ("email",)

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "is_staff",
        "is_active",
    )

    fieldsets = (
        (
            "User details",
            {"fields": ("email", "first_name", "last_name", "phone_number")},
        ),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
