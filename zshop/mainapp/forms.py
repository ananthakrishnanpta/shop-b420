from django import forms

from .models import Product 


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control w-50', 'placeholder' :'Product name'}),
            "price": forms.NumberInput(attrs={'class' : 'form-control w-50', 'value': 0.00}),
            "desc" : forms.TextInput(attrs={'class' : 'form-control'}),
            
        }