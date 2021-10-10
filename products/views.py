import itertools

from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from django.views.generic import CreateView

from django.views.generic import ListView, DetailView
from django.views import View

from .models import Product, Images, Comment, ProductGallery


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
