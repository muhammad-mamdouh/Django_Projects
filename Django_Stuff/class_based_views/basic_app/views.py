from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import School
from django.urls import reverse_lazy


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


class SchoolDetailView(DetailView):
    model = School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'


class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:schools_list')
