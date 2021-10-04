from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Carts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CartItems(models.Model):
    STATUS_CHOICES = (
        ("paid", "Paid"),
        ("pending", "Pending"),
    )
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="pending")
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
