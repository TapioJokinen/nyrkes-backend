from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from nyrkes.api.exceptions import APINotImplemented
from nyrkes.utils import converters


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

    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)
        self.data = converters.obj_to_camel_case(data)
