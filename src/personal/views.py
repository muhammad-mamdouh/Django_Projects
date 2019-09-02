from django.shortcuts import render
from blog.models import BlogPost
from operator import attrgetter

def home_screen_view(request):
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    return render(request, 'personal/home.html', {'blog_posts': blog_posts})
