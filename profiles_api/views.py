from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Testing API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            "Uses HTTP methods as a function (get, post, patch, put, delete)",
            "Is similar to traditional Django view",
            "Gives you most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message" : "Hello!", "an_apiview" : an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle a HTTP put request"""
        return Response({"mathod":"put"})

    def patch(self, request, pk=None):
        """Handle a HTTP patch request"""
        return Response({"mathod":"patch"})

    def delete(self, request, pk=None):
        """Habdle a HTTP delete request"""
        return Response({"method":"delete"})
