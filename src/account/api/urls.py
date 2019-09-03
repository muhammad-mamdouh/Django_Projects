from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


app_name    = 'account'
urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
]
