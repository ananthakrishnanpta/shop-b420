from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cart.models import CartItem
from mainapp.models import Product
from django.core.validators import RegexValidator

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    full_name = models.CharField(max_length=100, help_text="Full name of the recipient")
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits long.")
        ],
        help_text="Recipient's phone number"
    )
    address_line1 = models.CharField(max_length=255, help_text="Street address, P.O. Box, etc.")
    address_line2 = models.CharField(
        max_length=255, blank=True, null=True, help_text="Apartment, suite, unit, building, floor, etc."
    )
    landmark = models.CharField(
        max_length=255, blank=True, null=True, help_text="Landmark near the address"
    )
    city = models.CharField(max_length=100, help_text="City name")
    state = models.CharField(
        max_length=100,
        help_text="State name",
        choices=[
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    # Union Territories
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli and Daman and Diu", "Dadra and Nagar Haveli and Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Ladakh", "Ladakh"),
    ("Lakshadweep", "Lakshadweep"),
    ("Puducherry", "Puducherry"),
        ]
    )
    pincode = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(r'^\d{6}$', message="PIN code must be 6 digits long.")
        ],
        help_text="6-digit PIN code"
    )
    country = models.CharField(
        max_length=100, default="India", editable=False, help_text="Country name"
    )
    is_default = models.BooleanField(
        default=False, help_text="Set as the default address"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'pincode', 'address_line1', 'address_line2')

    def __str__(self):
        return f"{self.full_name}, {self.address_line1}, {self.city}, {self.state} - {self.pincode}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('PENDING','Pending'),('COMPLETED','Completed')])
    razorpay_order_id = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name="orders")

    def __str__(self):
        return f"Order #{self.id} for {self.user.username}"
    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name="order_details", on_delete=models.CASCADE)
    order_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for order {self.order.id} - Product: {self.order_item.product.name}"
    
    
