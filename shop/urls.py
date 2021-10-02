from django.contrib import admin
from django.urls import path, include

from .views import home_page

urlpatterns = [
    path('', home_page),
    path('', include('users.urls')),
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
]
