from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    return render(request, 'basicapp/form_page.html', {'form': form})
