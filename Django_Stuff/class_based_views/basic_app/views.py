from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import School


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'some_key': 'basic injection'
        }
        return context


class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'
