from django.urls import path

from nyrkes.api.views.user_organizations import UserOrganizations

urlpatterns = [
    path("organizations/", UserOrganizations.as_view(), name="user_organizations"),
]
