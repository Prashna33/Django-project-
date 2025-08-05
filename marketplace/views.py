from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from blogs.models import Blog, BlogCategory


def home(request):
    products = Product.objects.all()
    #blogs = Blogs.objects.all()[:3]
    Blogs = Blogs.objects.all()[:3]

    return render(request, 'extending/home.html', {
        'products': products, 
        'blogs': blogs
    })

