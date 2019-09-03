from django.urls import path
from . import views

app_name    = 'blog'
urlpatterns = [
    path('<slug:slug>/', views.api_detail_blog_view, name='detail'),
]
