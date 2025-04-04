from django.urls import path

# importing necessary views 
from .views import UserLogin, UserRegister

urlpatterns = [
    path('login', UserLogin.as_view(), name='signin'),
    path('register', UserRegister.as_view(), name='signup')
]

