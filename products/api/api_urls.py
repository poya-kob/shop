from django.urls import path, include
# from .api_views import ProductListserializer, ProductDetailserializer
from rest_framework.routers import SimpleRouter

from products.api.api_views import ProductViewSet

router = SimpleRouter()

router.register("products", ProductViewSet)

urlpatterns = [
    # path('products/', ProductListserializer.as_view(), name="product_list"),
    # path('products/<int:pk>/', ProductDetailserializer.as_view(), name="product_detail"),
    path('', include(router.urls)),
]
