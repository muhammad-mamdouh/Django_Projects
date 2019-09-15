from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import json
from .models import Project, Category, Expense
from .forms import ExpenseForm


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


def project_detail_view(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        return render(request, 'budget/project-detail.html', {
                       'project': project,
                       'expense_list': project.expenses.all(),
                       'category_list': category_list
                })

    elif request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            title         = form.cleaned_data['title']
            amount        = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']
            category      = get_object_or_404(Category, name=category_name, project=project)
            Expense.objects.create(project=project, title=title, amount=amount, category=category)

    elif request.method == 'DELETE':
        id      = json.loads(request.body)['id']
        expense = Expense.objects.get(id=id)
        expense.delete()
        return HttpResponse(status=204)

    return redirect(project)
