from django.urls import path
from .views import viewCart, addToCart

urlpatterns = [
    path('', viewCart, name='view_cart'),
    path('addCart/<int:product_id>', addToCart, name = 'add_to_cart')
]