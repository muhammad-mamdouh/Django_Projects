from django.urls import path
from . import views

app_name    = 'blog'
urlpatterns = [
    path('<slug:slug>/', views.api_detail_blog_view, name='detail'),
    path('create', views.api_create_blog_view , name='create'),
    path('<slug:slug>/update/', views.api_update_blog_view , name='update'),
    path('<slug:slug>/delete/', views.api_delete_blog_view , name='delete'),
]
