from django.http import HttpResponse
from django.shortcuts import render

from settings.models import SiteSetting
from .models import ContactUs

from contact.forms import CreateContactForm

from .tasks import summation


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get("full_name")
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        text = contact_form.cleaned_data.get("text")
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        contact_form = CreateContactForm()

    setting = SiteSetting.objects.first()

    context = {
        "contact_form": contact_form,
        "setting": setting
    }
    return render(request, "contact_us/contact_us_page.html", context)


################################################################################
def test_celery(request):
    summation.delay(5.5)
    return HttpResponse("ba celery anjam shod")
