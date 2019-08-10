from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
    path('', views.SchoolListView.as_view(), name='schools_list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='school_details'),
    path('create/', views.SchoolCreateView.as_view(), name='school_create'),
]
