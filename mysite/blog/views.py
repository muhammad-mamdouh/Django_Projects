from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    redirect_field_name = 'post_detail'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    redirect_field_name = 'post_detail'
    form_class = PostForm
    extra_context = {'post_edit': 'valid'}


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_draft_list.html'
    context_object_name = 'posts'
    redirect_field_name = 'post_detail'

    def get_queryset(self):
        return Post.objects.filter(date_published__isnull=True).order_by('date_created')
