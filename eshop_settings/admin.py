from django.contrib import admin

from .models import FooterSetting


@admin.register(FooterSetting)
class AdminFooterSetting(admin.ModelAdmin):
    list_display = ('__str__',
                    'country',
                    'city',
                    'address',
                    'phone_number',
                    'mobile_number',
                    'email',
                    'copy_right',
                    'about',
                    'active'
                    )
