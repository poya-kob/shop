from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ProductListSerializers, ProductDetailSerializers
from products.models import Product


# class ProductListserializer(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#
#
# class ProductDetailserializer(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers


class ProductViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()

    serializer_class = {
        "list": ProductListSerializers,
        "retrieve": ProductDetailSerializers,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action)
    #
    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return ProductListSerializers
    #     elif self.action == 'retrieve':
    #         return ProductDetailSerializers
