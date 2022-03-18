from django.contrib import admin

from .models import Product, ProductGallery


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', '__categories__', 'visit_count', 'active')
    list_filter = (['active', 'categories'])
    search_fields = ('title', 'description')


@admin.register(ProductGallery)
class AdminProductGallery(admin.ModelAdmin):
    list_display = ('__str__', 'active')
    list_filter = (['active'])
