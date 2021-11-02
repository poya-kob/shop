from django.db import models

from django.contrib.auth.models import User
from cart.models import CartItems


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order_id = models.CharField(max_length=300)
    payment_id = models.CharField(max_length=300)
    amount = models.IntegerField()
    date = models.CharField(default='-', max_length=300)
    card_number = models.CharField(default="****", max_length=100)
    idpay_track_id = models.IntegerField(default=0000)
    bank_track_id = models.TextField(default=0000)
    status = models.IntegerField(default=0)

    cart_items = models.ManyToManyField(CartItems)

    def __str__(self):
        return str(self.pk) + "  |  " + self.order_id + "  |  " + str(self.status)
