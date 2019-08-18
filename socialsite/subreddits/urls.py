from django.urls import path
from . import views

app_name = 'subreddits'

urlpatterns = [
    path('', views.ListSubreddits.as_view(), name='all'),
    path('new/', views.CreateSubreddit.as_view(), name='create'),
    path('posts/in/<slug:slug>/', views.SingleSubreddit.as_view(), name='single'),
    path('join/<slug:slug>/', views.JoinSubreddit.as_view(), name='join'),
    path('leave/<slug:slug>/', views.LeaveSubreddit.as_view(), name='leave'),
]
