from django.urls import path, include
from .views import contact_page

urlpatterns = [
    path('contact-us', contact_page),

]
