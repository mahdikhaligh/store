import itertools

from django.shortcuts import render
from eshop_settings.models import FooterSetting
from eshop_products.models import Product
from eshop_sliders.models import Slider


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home(request):
    slider = Slider.objects.all().filter(active=True)
    must_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    lasted_products = Product.objects.order_by('-id').all()[:8]
    context = {
        'title': 'Dark-Invo-Pro-Item',
        'sliders': slider,
        'must_visit': my_grouper(4, must_visit_products),
        'lasted_products': my_grouper(4, lasted_products),
    }

    return render(request, 'Home.html', context)


def footer(request):
    footer_setting = FooterSetting.objects.first()
    context = {
        'footer': footer_setting
    }
    return render(request, 'shared/Footer.html', context)


def header(request):
    header_setting = FooterSetting.objects.first()
    context = {
        'header': header_setting
    }
    return render(request, 'shared/Header.html', context)


def about(request):
    about_setting = FooterSetting.objects.first()
    context = {
        'setting': about_setting
    }

    return render(request, 'About.html', context)
