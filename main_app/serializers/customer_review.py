from rest_framework import serializers

from main_app.models import Review, Product


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerReviewSerializer(serializers.ModelSerializer):
    product = ProductReviewSerializer()

    class Meta:
        model = Review
        fields = '__all__'
