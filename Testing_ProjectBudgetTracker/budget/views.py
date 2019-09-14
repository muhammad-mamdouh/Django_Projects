from django.views.generic import ListView
from .models import Project


class ProjectsListView(ListView):
    model               = Project
    template_name       = 'budget/project-list.html'
    context_object_name = 'project_list'
