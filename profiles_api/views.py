from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Testing API View"""

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            "Uses HTTP methods as a function (get, post, patch, put, delete)",
            "Is similar to traditional Django view",
            "Gives you most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message" : "Hello!", "an_apiview" : an_apiview})
