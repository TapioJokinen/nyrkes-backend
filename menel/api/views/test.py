from rest_framework.response import Response

from menel.api.base import MenelView


class TestView(MenelView):
    def get(self, request):
        return Response(200)
