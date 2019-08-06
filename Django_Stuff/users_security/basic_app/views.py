from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm


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
