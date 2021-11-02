from django.urls import path, include
from .views import contact_page, test_celery

urlpatterns = [
    path('contact-us', contact_page),
    path('async-sum/', test_celery),

]
