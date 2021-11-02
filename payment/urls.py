from django.urls import path
from views import gateway, payment_return

urlpatterns = [
    path('gateway', gateway, name='gateway'),
    path('payment-return', payment_return, name='return')
]
