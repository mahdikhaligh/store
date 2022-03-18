from django.contrib import admin
from .models import Slider


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'description', 'active')
    list_filter = (['active'])
    search_fields = (['title'])
