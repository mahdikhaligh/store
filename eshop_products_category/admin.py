from django.contrib import admin

from .models import ProductCategory


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'active')
    list_filter = (['active'])
