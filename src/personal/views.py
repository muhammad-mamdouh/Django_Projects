from django.shortcuts import render
from blog.models import BlogPost
from blog.views import get_blog_queryset
from operator import attrgetter

def home_screen_view(request):
    query      = ''
    if request.GET:
        query = request.GET['q']

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    return render(request, 'personal/home.html', {'blog_posts': blog_posts, 'query': str(query)})
