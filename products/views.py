import itertools

from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from django.views import View
from cart.forms import CartAddProductForm

from .models import Product, Comment, ProductGallery

from .models import Product


class ProductList(ListView):
    queryset = Product.objects.filter(is_active=True, in_stock=True)
    template_name = 'products_temp/product_list.html'


def gallery_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ProductDetail(View):

    def get(self, request, pk):
        product_detail_qs = get_object_or_404(Product, id=pk)
        galleries = ProductGallery.objects.filter(product_id=pk)
        grouped_galleries = list(gallery_grouper(3, galleries))
        context = {
            "product_detail": product_detail_qs,
            "galleries": grouped_galleries,

        }
        return render(request, "products_temp/product_detail.html", context)

    def product_detail(request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)

        cart_product_form = CartAddProductForm()
        return render(request, 'cart/detail.html',
                      {'product': product, 'cart_product_form': cart_product_form})