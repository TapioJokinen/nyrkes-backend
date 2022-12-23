from rest_framework import status

from nyrkes.api.base import BaseAPIView, CamelCaseResponse


class UserOrganizations(BaseAPIView):
    def get(self, request):
        orgs = list(request.user.get_orgs().values())
        return CamelCaseResponse(data=orgs, status=status.HTTP_200_OK)
