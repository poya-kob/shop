from django.shortcuts import render

from decimal import Decimal
from datetime import datetime

import pytz
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from cart.models import Cart
from .models import Invoice
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from idpay.api import IDPayAPI

import uuid


def payment_init():
    base_url = config('BASE_URL', default='http://127.0.0.1:8000/', cast=str)
    api_key = config('IDPAY_API_KEY', default='18c5c450-563a-48b5-af03-4f1ad3d89b0c', cast=str)
    sandbox = config('IDPAY_SANDBOX', default=True, cast=bool)

    return IDPayAPI(api_key, base_url, sandbox)


def payment_start(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user_id=request.user.id)
        order_id = uuid.uuid1()
        amount = 0
        cart_items_id = []
        for item in cart.cart_items.filter(status="pending"):
            amount += item.get_cost
            cart_items_id.append(item.id)

        payer = {
            'name': f'{request.user.first_name} {request.user.last_name}'
            # todo:user name and last name handler in profile

        }

        record = Invoice(user_id=request.user.id, order_id=order_id, amount=int(amount))
        record.save()
        record.cart_items.add(*cart_items_id)
        record.save()

        idpay_payment = payment_init()
        result = idpay_payment.payment(str(order_id), amount, 'payment-return/', payer)

        if 'id' in result:
            record.status = 1
            record.payment_id = result['id']
            record.save()

            return redirect(result['link'])

        else:
            txt = result['message']
    else:
        txt = "Bad Request"

    return render(request, 'payment_temp/error.html', {'txt': txt})


@csrf_exempt
def payment_return(request):
    if request.method == 'POST':

        pid = request.POST.get('id')
        status = request.POST.get('status')
        pidtrack = request.POST.get('track_id')
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        card = request.POST.get('card_no')
        date = request.POST.get('date')

        if Invoice.objects.filter(order_id=order_id, payment_id=pid, amount=amount, status=1).count() == 1:

            idpay_payment = payment_init()
            payment = Invoice.objects.get(payment_id=pid, amount=amount)
            payment.status = status
            payment.date = datetime.fromtimestamp(int(date)).replace(tzinfo=pytz.UTC)
            payment.card_number = card
            payment.idpay_track_id = pidtrack
            payment.save()

            if str(status) == '10':
                result = idpay_payment.verify(pid, payment.order_id)

                if 'status' in result:

                    payment.status = result['status']
                    payment.bank_track_id = result['payment']['track_id']
                    payment.save()
                    # todo: inventory inc , cart item status = paid
                    # if result['status'] == 100:
                    #     payment.update(status='paid')
                    return render(request, 'payment_temp/error.html', {'txt': result['message'],
                                                                       'payment': payment,

                                                                       })

                else:
                    txt = result['message']

            else:
                txt = "Error Code : " + str(status) + "   |   " + "Description : " + idpay_payment.get_status(status)

        else:
            txt = "Order Not Found"

    else:
        txt = "Bad Request"

    return render(request, 'payment_temp/error.html', {'txt': txt})


def payment_check(request, pk):
    payment = Invoice.objects.get(pk=pk)
    idpay_payment = payment_init()
    result = idpay_payment.inquiry(payment.payment_id, payment.order_id)

    if 'status' in result:
        payment.status = result['status']
        payment.idpay_track_id = result['track_id']
        payment.bank_track_id = result['payment']['track_id']
        payment.card_number = result['payment']['card_no']
        payment.date = str(result['date'])
        payment.save()

    return render(request, 'payment_temp/error.html', {'txt': result['message']})
