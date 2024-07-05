from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
# we will be using CRUD here.

# Home View
def home_view(request):
    return render (request, 'siteApp/home.html')

# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('product_list')
    return render (request, 'siteApp/product_form.html', {'form': form})

# Read View
def product_list_view(request):
    product = Product.objects.all()
    return render (request, 'siteApp/product_list.html', {'product': product})

# Update View
def product_update_view (request, product_id):
    product = Product.objects.get(product_id = product_id)
    form = ProductForm ()
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect ('product_list')
    return render (request, 'siteApp/product_form.html', {'form': form})
    
# Delete View
def product_delete_view (request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect ('product_list')
    return render (request, 'siteApp/confirm_delete.html', {'product': product})