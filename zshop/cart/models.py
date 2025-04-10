from django.db import models

# importing the Product model from mainapp as it is a foreign key for CartItem
from mainapp.models import Product

# importing the User model from django.contrib.auth as it is also a foreign key
from django.contrib.auth.models import User 

# Create your models here.
class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    user = models.ForeignKey(User, on_delete = models.CASCADE)

    quantity = models.IntegerField(default=0)
    # INTEGER
    
    date_added = models.DateTimeField(auto_now_add=True)
    # Current timestamp


    def __str__(self):
        return f"{self.product.name} added by {self.user.username} at {self.date_added}"
