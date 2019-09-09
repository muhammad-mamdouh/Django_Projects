from django.views.generic import TemplateView


class SignInView(TemplateView):
    template_name = 'login.html'


class HomeView(TemplateView):
    template_name = 'index.html'
