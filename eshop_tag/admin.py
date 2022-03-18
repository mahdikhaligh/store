from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'time', 'active')
    list_filter = (['active', 'time'])
