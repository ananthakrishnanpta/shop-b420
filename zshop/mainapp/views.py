from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from .models import Product

# Create your views here.


def homeView(request):
    # template 
    template = loader.get_template('home.html')

    # context data
    context = {
        # context data to be pulled from the DB
        'products' : Product.objects.all()
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return HttpResponse(template.render(context, request))

def aboutView(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))