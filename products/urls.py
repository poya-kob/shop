from django.urls import path, include
from .views import ProductList, ProductDetail, add_comment_view, delete_comment,SearchProductsView

urlpatterns = [
    path('', ProductList.as_view(), name="product_list"),
    path('<int:pk>/', ProductDetail.as_view(), name="product_detail"),
    path('add_comment/', add_comment_view, name="add_comment"),
    path('delete_comment/<int:pk>', delete_comment, name="delete_comment"),
    path('search/', SearchProductsView.as_view()),
]
