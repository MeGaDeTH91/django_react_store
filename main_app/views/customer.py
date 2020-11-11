from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main_app.models import Customer
from main_app.serializers.customer import CustomerSerializer, CustomerSerializerWithToken


@api_view(['GET'])
def authenticate_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = CustomerSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_users(request):
    users = Customer.objects.all()
    serializer = CustomerSerializer(users, many=True)
    return Response(serializer.data)


class CustomerList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CustomerSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
