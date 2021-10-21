import itertools

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.views.generic import ListView, DetailView, CreateView

from django.views.generic.edit import DeleteView
from django.views import View
from cart.forms import CartAddProductForm

from .models import Product, Comment, ProductGallery

from .models import Product


class ProductList(ListView):
    queryset = Product.objects.filter(is_active=True, in_stock=True)
    template_name = 'products_temp/product_list.html'
    paginate_by = 3


def gallery_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ProductDetail(View):

    def get(self, request, pk):
        product_detail_qs = get_object_or_404(Product, id=pk)
        related_product = Product.objects.filter(category=product_detail_qs.category).distinct()
        grouped_related_products = gallery_grouper(3, related_product)
        galleries = ProductGallery.objects.filter(product_id=pk)
        grouped_galleries = list(gallery_grouper(3, galleries))
        context = {
            "product_detail": product_detail_qs,
            "galleries": grouped_galleries,
            "related_product": grouped_related_products,

        }
        return render(request, "products_temp/product_detail.html", context)

    def product_detail(request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)

        cart_product_form = CartAddProductForm()
        return render(request, 'cart/detail.html',
                      {'product': product, 'cart_product_form': cart_product_form})


@login_required()
@require_http_methods(["POST"])
def add_comment_view(request):
    title = request.POST.get('title')
    email = request.POST.get('email')
    pid = request.POST.get('pid')
    content = request.POST.get('content')
    Comment.objects.create(title=title, email=email, product_id=pid, content=content, user_id=request.user.id)
    return redirect(reverse('product_detail', args=pid))


@login_required()
@require_http_methods(["POST"])
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('product_detail', pk=comment.product.pk)


class SearchProductsView(ListView):
    template_name = "products_temp/product_list.html"
    paginate_by = 3

    def get_queryset(self):
        request = self.request
        query = request.GET.get("q")
        if query is not None:
            return Product.objects.filter(is_active=True, in_stock=True, name__icontains=query)
        return Product.objects.get_active_products()
