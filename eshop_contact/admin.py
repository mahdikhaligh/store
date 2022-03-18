from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('fullname',  'email', 'subject', 'time', 'is_read')
    list_filter = (['is_read', 'time'])
    search_fields = ('fullname', 'subject')

