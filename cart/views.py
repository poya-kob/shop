from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart, CartItems


@require_POST
def cart_add(request, product_id):
    count = request.POST.get('count')
    if not Cart.objects.filter(user_id=request.user.id):
        Cart.objects.create(user_id=request.user.id)
    cart = Cart.objects.get(user_id=request.user.id)
    product = get_object_or_404(Product, id=product_id)
    cart.cart_items.create(product=product, quantity=int(count), price=product.price)
    return redirect(reverse('cart_detail'))

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    product_id = str(product.id)
    if product_id in cart:
        # Subtract 1 from the quantity
        cart[product_id]['quantity'] -= 1
        # If the quantity is now 0, then delete the item
        if cart[product_id]['quantity'] == 0:
            del cart[product_id]
            cart.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart, status = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItems.objects.filter(cart=cart)

    context = {
        'cart_item': cart_item,
    }

    return render(request, 'cart/detail.html', context)
