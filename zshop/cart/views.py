from django.shortcuts import render, redirect
from django.template import loader
from .models import CartItem
from mainapp.models import Product


# Create your views here

def viewCart(request):

    # select * from CartItem where user = request.user; 
    # => this gives reference to collection of cart items (filter)
    cartItems = CartItem.objects.filter(user = request.user)  

    template = 'cart.html'

    context = {
        'items' : cartItems
    }

    return render(request, template, context)

def addToCart(request, product_id):

    # select * from Product where id = product_id; 
    # => Gives reference to individual object (get)
    this_product = Product.objects.get(id = product_id)
    
    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1

    cart_item.save() # insert or update the particular record

    return redirect('view_cart')
