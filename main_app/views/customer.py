from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main_app.middleware.authenticate_admin_middleware import authenticate_admin_middleware
from main_app.middleware.authenticate_guest_middleware import authenticate_guest_middleware
from main_app.models import Customer
from main_app.serializers.customer import CustomerSerializer, CustomerSerializerWithToken


@api_view(['GET'])
def authenticate_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = CustomerSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerRegister(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    @method_decorator(authenticate_admin_middleware)
    def get(self, request):
        users = Customer.objects.all()
        serializer = CustomerSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(authenticate_guest_middleware)
    def post(self, request, format=None):
        serializer = CustomerSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
