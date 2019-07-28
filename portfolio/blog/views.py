from django.shortcuts import render, get_object_or_404
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts': posts})


def post_detail(request, blog_id):
    post_details = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/post_details.html', {'post': post_details})
