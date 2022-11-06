from rest_framework.response import Response

from nyrkes.api.base import BaseAPIView


class TestView(BaseAPIView):
    def get(self, request):
        return Response(200)
