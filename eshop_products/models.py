import os
import random
from django.db import models
from django.db.models import Q

from eshop_products_category.models import ProductCategory


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)

    return name, ext


def upload_image_path(instance, filepath):
    new_name = random.randint(100000, 999999)
    name, ext = get_filename_ext(filepath)
    final_name = f"{new_name}-{instance.title}{ext}"

    return f"products/{final_name}"


def upload_image_gallery_path(instance, filepath):
    new_name = random.randint(100000, 999999)
    name, ext = get_filename_ext(filepath)
    final_name = f"{new_name}-{instance.title}{ext}"

    return f"products/galleries/{final_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(active=True, id=product_id)

        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tag__title__icontains=query)

        )

        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    visit_count = models.IntegerField(default=' ')

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ','-')}"

    def __categories__(self):
        name = self.categories.all()
        return name[0]


class ProductGallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_image_gallery_path)
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
