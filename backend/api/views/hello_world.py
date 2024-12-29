from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, World!"})
