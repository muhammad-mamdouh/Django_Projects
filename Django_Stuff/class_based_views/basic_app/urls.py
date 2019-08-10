from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.SchoolListView.as_view(), name='schools_list'),
]
