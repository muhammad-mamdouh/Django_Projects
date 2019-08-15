from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import  UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
