from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from nyrkes.api.exceptions import APINotImplemented
from nyrkes.utils.converters import obj_to_camel_case


class BaseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        raise APINotImplemented

    def post(self, request):
        raise APINotImplemented

    def put(self, request):
        raise APINotImplemented

    def patch(self, request):
        raise APINotImplemented

    def delete(self, request):
        raise APINotImplemented


class CamelCaseResponse(Response):
    """Converts response body to camel case."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = obj_to_camel_case(kwargs["data"])
