from django.contrib import admin

# importing the necessary models of the app here

from .models import Product

# Register your models here.
# Every model registered here, will be available in django's prebuilt admin panel

admin.site.register(Product)