from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from rest_framework.response import Response

from ..middleware.auth_middleware import jwt_auth_middleware
from ..middleware.login_required_middleware import login_required_middleware
from ..models import Product
from ..serializers.product import ProductSerializer


class ListProductsView(APIView):
    @method_decorator(login_required_middleware)
    def get(self, req):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @method_decorator(jwt_auth_middleware)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
