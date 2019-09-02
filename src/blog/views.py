from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required
from .forms import CreateBlogPostForm
from .models import BlogPost
from account.models import Account


# @login_required
def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj        = form.save(commit=False)
        author     = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        return redirect('personal:home-page')

    context['form'] = form
    return render(request, 'blog/create_blog.html', context)


def detail_blog_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail_blog.html', {'blog_post': blog_post})
