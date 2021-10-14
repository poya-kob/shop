from django.shortcuts import render
from sliders.models import Slider


def header(request, *args, **kwargs):
    context = {
        "title": "this is title"
    }
    return render(request, "shared/Header.html", context)


def footer(request, *args, **kwargs):
    context = {
        "about_us": "این سایت فروشگاهی به وسیله ی django ایجاد شده است",
    }
    return render(request, "shared/Footer.html", context)


def home_page(request):
    sliders = Slider.objects.all()

    context = {
        "data": "این سایت فروشگاهی با فریم ورک django نوشته شده است",
        "sliders": sliders
    }
    return render(request, "home_page.html", context)
