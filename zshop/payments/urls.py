from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('create_order/<int:order_id>/', views.create_razorpay_order, name='create_razorpay_order'),
    path('success/', views.payment_success, name='payment_success'),
    path('failure/', views.payment_failure, name='payment_failure'),  # Added route for payment failure
    # path('confirm-order/<int:order_id>/', views.confirm_order, name='confirm_order'),
]
