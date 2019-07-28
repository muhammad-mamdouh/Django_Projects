from django.urls import path
from .views import posts_list, post_detail

urlpatterns = [
    path('', posts_list, name='all_posts'),
    path('<int:blog_id>/', post_detail, name='detailed_post')
]