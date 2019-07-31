from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['user_password']
        confirmed_password = request.POST['user_confirm_password']
        if password == confirmed_password:
            try:
                User.objects.get(username=username)
                return render(request, 'accounts/signup.html',
                              {'username_error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                auth.login(request, user)
                messages.success(request, f"Account created for {username}!")
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',
                          {'confirm_password_error': "Password doesn't match"})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['user_password'])
        if user:
            auth.login(request, user)
            messages.success(request, 'Logged Successfully!')
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                          {'error_message': "Check your credentials! Username and password doesn't match"})
    else:
        return render(request, 'accounts/login.html')
