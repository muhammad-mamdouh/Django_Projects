from django.urls import path
from . import views


app_name    = 'budget'
urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='list'),
    path('add/', views.ProjectsCreateView.as_view(), name='add'),
]
