from django.contrib import admin
from .models import Payment

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('order', 'status', 'razorpay_payment_id', 'razorpay_order_id')
#     search_fields = ('order__id', 'razorpay_payment_id', 'razorpay_order_id')
