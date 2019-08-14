from django.views.generic import (
    TemplateView,
    ListView
)
from .models import Post


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
