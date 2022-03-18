from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_id = models.CharField(max_length=100, default=0)
    is_paid = models.BooleanField()
    payment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.owner.get_username()

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    def __product__(self):
        return '%s' % self.product.title

    def __order_user__(self):
        return '%s' % self.order.owner.get_username()

    def get_detail_sum(self):
        return self.count * self.price
