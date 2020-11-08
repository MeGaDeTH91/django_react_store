from rest_framework.views import APIView

from rest_framework.response import Response

from ..models import Product
from ..serializers.product import ProductSerializer


class ListProductsView(APIView):
    def get(self, req):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
