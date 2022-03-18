import itertools
from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404

from .models import Product, ProductGallery

from eshop_products_category.models import ProductCategory

from eshop_order.forms import UserNewOrderForm


class Product_List(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()

        if category is None:
            raise Http404('this category is not found')
        return Product.objects.get_products_by_category(category_name)


def my_grouper_gallery(n, iterable):
    args = [iter(iterable)] * n

    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    _product_id = kwargs['productid']

    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': _product_id})

    product: Product = Product.objects.get_by_id(_product_id)

    if product is None or not product.active:
        raise Http404('this is not found product')
    product.visit_count += 1
    product.save()

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
    grouped_related_products = list(my_grouper_gallery(4, related_products))

    galleries = ProductGallery.objects.filter(product_id=_product_id, active=True)
    grouped_galleries = list(my_grouper_gallery(3, galleries))

    context = {
        'product': product,
        'galleries': grouped_galleries,
        'related_products': grouped_related_products,
        'new_order_form': new_order_form
    }

    return render(request, 'products/product_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 100

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')

        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()


def product_category(request):
    categories = ProductCategory.objects.filter(active=True)
    context = {
        'categories': categories
    }

    return render(request, 'products/product_category.html', context)