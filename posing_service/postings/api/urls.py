from django.urls import path
from .views import BlogPostRUDView

app_name = 'api-postings'
urlpatterns = [
    path('<int:pk>/', BlogPostRUDView.as_view(), name='post-rud'),
]
