from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy

# importing custom form
from .forms import CustomLoginForm, CustomRegisterForm

# importing the inbuilt user LoginView to inherit and override the form and template
from django.contrib.auth.views import LoginView

# Create your views here.
class UserRegister(CreateView):
    form_class = CustomRegisterForm
    template_name = 'signup.html'
    # find the sign-in page path on successful registration and send the user there
    success_url = reverse_lazy('signin') 

class UserLogin(LoginView):
    template_name = 'signin.html'
    form_class = CustomLoginForm