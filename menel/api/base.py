from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from menel.api.exceptions import APINotImplemented


class MenelView(APIView):
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
