from django.contrib import admin
from .models import Order, OrderDetail


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('__str__', 'is_paid', 'payment_date')
    list_filter = (['is_paid', 'payment_date'])
    search_fields = ('is_paid', 'payment_date')


@admin.register(OrderDetail)
class AdminOrderDetail(admin.ModelAdmin):
    list_display = ('__order_user__', '__product__', 'price', 'count')
    search_fields = (['__str__'])
