from rest_framework import serializers
from products.models import Product

# class ProductSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"

from rest_framework.serializers import StringRelatedField


class ProductListSerializers(serializers.HyperlinkedModelSerializer):
    category = StringRelatedField()

    class Meta:
        model = Product
        fields = ["url", "category", "name", "price"]


class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
