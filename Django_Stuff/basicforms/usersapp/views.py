from django.shortcuts import render, redirect
from .forms import NewUserForm


def users(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewUserForm()
    return render(request, 'usersapp/users.html', {'form': form})
