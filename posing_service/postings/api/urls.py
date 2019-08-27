from django.urls import path
from .views import BlogPostRUDView, BlogPostAPIView, BlogPostListView

app_name = 'api-postings'
urlpatterns = [
    path('all/', BlogPostListView.as_view(), name='post-list'),
    path('', BlogPostAPIView.as_view(), name='post-create'),
    path('<int:pk>/', BlogPostRUDView.as_view(), name='post-rud'),
]
