from django import forms
from siteApp import models

class ProductForm (forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        labels = {
            'product_id': 'Product_Id',
            'product_name': 'Product_Name',
            'sku': 'Sku',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier_name': 'Supplier_Name'
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs= {'placeholder':'e.g 1', 'class':'form-control'}),
            'product_name': forms.TextInput(
                attrs= {'placeholder':'e.g shirt', 'class':'form-control'}),
            'sku': forms.TextInput(
                attrs= {'placeholder':'e.g S12345', 'class':'form-control'}),
            'price': forms.NumberInput(
                attrs= {'placeholder':'e.g 19.00', 'class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs= {'placeholder':'e.g 10', 'class':'form-control'}),
            'supplier_name': forms.TextInput(
                attrs= {'placeholder':'e.g ABC Corp', 'class':'form-control'}),
        }