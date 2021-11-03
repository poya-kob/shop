from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart


@require_POST
def cart_add(request, product_id):
    count = int(request.POST.get('count'))
    if not Cart.objects.filter(user_id=request.user.id):
        Cart.objects.create(user_id=request.user.id)
    cart = Cart.objects.get(user_id=request.user.id)
    product = get_object_or_404(Product, id=product_id)
    cart_item = cart.cart_items.filter(product_id=product_id).first()
    if cart_item:
        if product.inventory > (count + cart_item.quantity):
            cart_item.quantity += count
            cart_item.save()
        else:
            raise Exception("تعداد بیشتر از موجودی")
    else:
        cart.cart_items.create(product_id=product_id, quantity=int(count), price=product.price)
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
    context = {
        'cart_item': cart.cart_items.filter(status='pending'),

    }

    return render(request, 'cart/checkout.html', context)
