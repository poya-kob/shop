from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CartItems(models.Model):
    STATUS_CHOICES = (
        ("paid", "پرداخت شده"),
        ("pending", "پرداخت نشده"),
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="pending")
    is_selected = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        if self.product.inventory < self.quantity:
            raise Exception("in tedad nadarim")
        self.price = self.product.price
        super().save(*args, **kwargs)

    @property
    def get_cost(self):
        return self.price * self.quantity
