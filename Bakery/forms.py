from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Chocolate Croissant',
                'aria-label': 'Product name',
                'required': 'required'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'step': '0.01',
                'min': '0',
                'placeholder': '0.00',
                'aria-label': 'Price in INR',
                'required': 'required'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Short description of the product',
                'aria-label': 'Product description'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input',
                'accept': 'image/*',
                'aria-label': 'Product image'
            }),
        }
