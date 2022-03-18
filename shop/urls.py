from django.contrib import admin
from django.urls import path, include

from . import settings
from django.conf.urls.static import static

from .views import home, header, footer, about

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('about', about),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),

    path('', include('eshop_account.urls')),
    path('', include('eshop_contact.urls')),
    path('', include('eshop_products.urls')),
    path('', include('eshop_order.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
