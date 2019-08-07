from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registerd = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)    # Hashing the password
            user.save()

            profile = profile_form.save(commit=False)   # Don't save yet, saving will overwrite the last user record
            profile.user = user     # Setting up the OneToOne relationship
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registerd = True    # Registered Successfully
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'registerd': registerd,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'basic_app/registration.html', context=context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Account Not Active")
        else:
            print('Someone tried to login and failed')
            print(f'Username: {username}, Password: {password}')
            return HttpResponse('Invalid login credentials supplied')
    else:
        return render(request, 'basic_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
