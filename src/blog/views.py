from django.shortcuts import render
from .models import BlogPost


def create_blog_view(request):
    return render(request, 'blog/create_blog.html')