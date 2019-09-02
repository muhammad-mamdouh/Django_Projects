from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .forms import CreateBlogPostForm, UpdateBlogPostForm
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


def edit_blog_view(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, f'Your post has been updated!')
            return redirect('blog:detail', slug=obj.slug)

    form = UpdateBlogPostForm(
            initial={
                'title': blog_post.title,
                'body': blog_post.body,
                'image': blog_post.image,
            }
        )
    return render(request, 'blog/edit_blog.html', {'form': form})
