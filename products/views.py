from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views import View
from cart.forms import CartAddProductForm

from .models import Product


class ProductList(View):
    def get(self, request):
        products_list_qs = Product.objects.filter(is_active=True, in_stock=True)

        context = {
            "Product_list": products_list_qs
        }
        return render(request, "products_temp/product_list.html", context)


class ProductDetail(View):

    def get(self, request, pk):
        product_detail_qs = get_object_or_404(Product, id=pk)
        context = {
            "product_detail": product_detail_qs,
        }
        return render(request, "products_temp/product_detail.html", context)

    def product_detail(request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)

        cart_product_form = CartAddProductForm()
        return render(request,'cart/detail.html',
                      {'product': product,'cart_product_form': cart_product_form})