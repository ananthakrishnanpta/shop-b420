from django.urls import path

from . import views

urlpatterns = [
    # path('<urlPattern>', views.<viewFunction>, name = '<path_reference_name>')
    path('', views.homeView, name = 'homepage'),
    path('about', views.aboutView, name = 'aboutpage'),
    path('contact', views.contactView, name = 'contactpage')

]