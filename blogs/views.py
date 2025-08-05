from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogCategory

# View to list all blogs
def blogs(request):
    all_blogs = Blog.objects.all()
    return render(request, 'basic/blogs.html', {'blogs': all_blogs})

# View to show details of a single blog
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'basic/blogs_details.html', {'blog': blog})
