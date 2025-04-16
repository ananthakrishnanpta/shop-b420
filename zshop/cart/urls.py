from django.urls import path
from .views import viewCart, addToCart, remFromCart

urlpatterns = [
    path('', viewCart, name='view_cart'),
    path('addCart/<int:product_id>', addToCart, name = 'add_to_cart'),
    path('remCart/<int:cart_item_id>', remFromCart, name = 'rem_from_cart')
]