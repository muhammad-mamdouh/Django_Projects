from django.urls import path
from .views import BlogPostRUDView, BlogPostAPIView

app_name = 'api-postings'
urlpatterns = [
    path('', BlogPostAPIView.as_view(), name='post-create'),
    path('<int:pk>/', BlogPostRUDView.as_view(), name='post-rud'),
]
