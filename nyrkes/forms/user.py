from django.contrib.auth import forms

from nyrkes.models import User


class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
