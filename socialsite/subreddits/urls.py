from django.urls import path
from . import views

app_name = 'subreddits'

urlpatterns = [
    path('', views.ListSubreddits.as_view(), name='all'),
    path('new/', views.CreateSubreddit.as_view(), name='create'),
]
