from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from django.utils import timezone
from .models import Post


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')


class PostDetailView(DetailView):
    model = Post
