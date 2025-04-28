from django.urls import path
from . import views


urlpatterns = [
    # Route to create a new order
    path('create/', views.create_order, name='create_order'),
    
    # Route to display the user's order history
    path('orders/history/', views.order_history, name='order_history'),
    
    # Route to order history version 2
    path('orders/history/v2', views.order_history_2, name='order_history_2'),
    
    # Route to view details of a specific order
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    
    # Route to add a new address
    path('address/add/', views.add_address, name='add_address'),
    
    # Route to select an address for an order
    path('address/select/<int:order_id>/', views.select_address_for_order, name='select_address_for_order'),
    
    # Route to update an existing order (optional, based on the `update_order` view)
    path('update/<int:order_id>/', views.update_order, name='update_order'),
    
    path('order/cancel/<int:order_id>', views.cancel_order, name='cancel_order')
]
