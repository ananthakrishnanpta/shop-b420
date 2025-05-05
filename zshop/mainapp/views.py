from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product

from .forms import AddProductForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def homeView(request):
    # template 
    template = loader.get_template('home.html')

    # context data
    context = {
        # context data to be pulled from the DB
        'products' : Product.objects.all(),
        # the above line of code is equivalent to SELECT * FROM product_table;
        'search_bar' : True,
        'current_page' : 'home'
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



# CRUD Operations

# Read operation we have already explored above,
# Let's explore the other operations

# Create

class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = AddProductForm
    # This view on successful addition of products, redirects the user to a 
    # new page, to set this page, we do the below line of code
    success_url = '/'

# U - Update

class EditProduct(UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'edit_product.html'
    fields = ['img','price', 'stock', 'desc']
    success_url = '/'

# D - Delete


class DelProduct(DeleteView):
    model = Product
    template_name = 'del_product.html'
    success_url = '/'




def searchView(request):
    query = request.GET.get('search_text')

    result_products = Product.objects.filter(name__icontains = query)
    context =  {
        'prods' : result_products,
        'query' : query,
        'search_bar' : True
    }

    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context, request))
