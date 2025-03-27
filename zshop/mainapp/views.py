from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView

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

# The above view can be implemented using CBV as below

# class HomeView(ListView):
#     model = Product
#     template_name = 'home.html'
#     context_object_name = 'products'

class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'
    
# The same view above can be implemented like below too using FBV

# def productDetail(request, id):
#     products = Product.objects.get(id=id)
#     context = {
#         'products' : products
#     }
#     template = loader.get_template('product_details.html')
#     return HttpResponse(template.render(context, request))

def aboutView(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))