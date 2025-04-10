from django.shortcuts import render
from django.template import loader
from .models import CartItem


# Create your views here

def viewCart(request):
    cartItems = CartItem.objects.filter(user = request.user)

    template = 'cart.html'

    context = {
        'items' : cartItems
    }

    return render(request, template, context)