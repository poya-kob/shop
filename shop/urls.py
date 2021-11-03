from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import home_page, header, footer, about_page
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', home_page),
    path('', include('users.urls')),
    path('', include('contact.urls')),
    path('about-us', about_page),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('cart/', include('cart.urls')),
    path('products/', include('products.urls')),
    path('', include('payment.urls')),
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include("products.api.api_urls")),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)