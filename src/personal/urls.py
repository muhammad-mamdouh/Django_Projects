from django.urls import path
from . import views

app_name    = 'personal'
urlpatterns = [
    path('', views.home_screen_view, name='home-page')
]
