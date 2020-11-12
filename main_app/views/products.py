from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from rest_framework.response import Response

from ..middleware.authenticate_admin_middleware import authenticate_admin_middleware
from ..models import Product
from ..serializers.product import ProductSerializer


class ListProductsView(APIView):
    def get(self, req):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @method_decorator(authenticate_admin_middleware)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
