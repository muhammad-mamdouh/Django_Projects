from django.views.generic import ListView, CreateView
from .models import Project, Category


class ProjectsListView(ListView):
    model               = Project
    template_name       = 'budget/project-list.html'
    context_object_name = 'project_list'


class ProjectsCreateView(CreateView):
    model         = Project
    template_name = 'budget/add-project.html'
    fields        = ['name', 'budget']

    def form_valid(self, form):
        self.object = form.save()
        categories  = self.request.POST.get('categoriesString').split(',')
        for category in categories:
            Category.objects.create(
                name=category,
                project=Project.objects.get(id=self.object.id)
            )
        return super().form_valid(form)
