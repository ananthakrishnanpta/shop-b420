from django.urls import path
from .views import viewCart, addToCart, remFromCart, addQuantity, remQuantity

urlpatterns = [
    path('', viewCart, name='view_cart'),
    path('addCart/<int:product_id>', addToCart, name = 'add_to_cart'),
    path('remCart/<int:cart_item_id>', remFromCart, name = 'rem_from_cart'),
            # The following url patterns will be requested by the JS function
    path('add/<int:cart_item_id>', addQuantity, name='add_quantity'),
    path('remove/<int:cart_item_id>', remQuantity, name='rem_quantity'),
]