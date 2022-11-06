from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from nyrkes.api.exceptions import APINotImplemented


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
