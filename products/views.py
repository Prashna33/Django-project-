from django.shortcuts import render, get_object_or_404
from . models import Category, Product

def product(request):
    all_products = Product.objects.all()
    return render(request, 'extending/products.html', {'products': all_products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'extending/product_details.html', {'product': product})
  