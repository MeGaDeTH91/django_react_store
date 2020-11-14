from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main_app.middleware.authenticate_user_middleware import authenticate_user_middleware
from main_app.models import Customer
from main_app.serializers.customer import CustomerSerializer
from main_app.serializers.profile import ProfileSerializer


@api_view(['GET'])
@authenticate_user_middleware
def profile_details(request, pk):
    if request.user.id != pk:
        return Response('You are not allowed to perform this action.', status=status.HTTP_401_UNAUTHORIZED)
    user = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileEdit(APIView):
    """
    Profile edit view.
    """

    @method_decorator(authenticate_user_middleware)
    def get(self, request, pk):
        if request.user.id != pk:
            return Response('You are not allowed to perform this action.', status=status.HTTP_401_UNAUTHORIZED)
        user = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(authenticate_user_middleware)
    def put(self, request, pk, format=None):
        if request.user.id != pk:
            return Response('You are not allowed to perform this action.', status=status.HTTP_401_UNAUTHORIZED)
        user = Customer.objects.get(pk=pk)
        serializer = ProfileSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
