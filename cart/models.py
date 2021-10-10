from django.contrib.auth.models import User
from django.db import models

from products.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
        return int(total)

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    STATUS_CHOICES = (
                ("paid", "Paid"),
                ("pending", "Pending"),
            )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='cartitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="pending")
    is_selected = models.BooleanField(default=False)

    @property
    def total_price(self):
        return int(self.price * self.quantity)

    def __str__(self):
        return self.product.name