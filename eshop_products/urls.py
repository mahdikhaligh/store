from django.urls import path

from .views import Product_List, product_detail, SearchProducts, ProductsListByCategory, product_category


urlpatterns = [
    path('products', Product_List.as_view()),
    path('products/search', SearchProducts.as_view()),

    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('product_category', product_category, name='product_category'),

    path('products/<productid>/<title>', product_detail)
]
