from rest_framework import serializers

from main_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Product
        fields = '__all__'
