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


class PostDetailView(DetailView):
    model = Post
