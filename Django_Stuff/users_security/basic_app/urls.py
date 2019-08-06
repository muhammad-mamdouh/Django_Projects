from django.urls import path
from . import views

# Template URLs!
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
]
