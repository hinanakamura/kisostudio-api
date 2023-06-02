from rest_framework import serializers
from .models import CATEGORY, PRODUCT, IMAGE

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CATEGORY
        fields = (
            "id",
            "category_name",
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUCT
        fields = (
            "id",
            "product_name",
            "stripe_id",
            "stock_count",
            "thumbnail",
            "category",
            "pub_date",
        )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMAGE
        fields = (
            "image",
            "product",
            "order"
        )