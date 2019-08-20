from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

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
        """Handle a HTTP delete request"""
        return Response({"method":"delete"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "Uses actions(list, create, retrive, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provide more functionality with more codes",
        ]

        return Response({"message":"Hello", "a_viewset":a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}!'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object"""
        return Response({"http_method":"GET"})

    def update(self, request, pk=None):
        """handle updating an object"""
        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """handle deleting an object"""
        return Response({"http_method":"DELETE"})
