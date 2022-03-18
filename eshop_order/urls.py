from django.urls import path
from .views import add_user_order, user_open_order, remove_order_detail, send_request, verify


urlpatterns = [
    path('add-user-order', add_user_order),
    path('user-open-order', user_open_order),
    path('remove-item/<detail_id>', remove_order_detail),
    path('payment_section', send_request),
    path('verify/<order_id>', verify)
]
