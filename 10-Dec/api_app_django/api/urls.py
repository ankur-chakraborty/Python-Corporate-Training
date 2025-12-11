from django.urls import path
from .views import get_products, get_product, create_product, update_product, delete_product

urlpatterns = [
    path('products/', get_products),
    path('products/<int:id>/',get_product),
    path('products/create/',create_product),
    path('products/update/<int:id>/',update_product),
    path('products/delete/<int:id>/',delete_product),
]