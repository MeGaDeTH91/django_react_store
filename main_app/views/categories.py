from rest_framework.views import APIView

from rest_framework.response import Response

from ..models import Category
from ..serializers.category import CategorySerializer


class ListCategoriesView(APIView):
    def get(self, req):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
