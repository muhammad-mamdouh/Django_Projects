from django.urls import path
from . import views

app_name    = 'account'
urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('must_authenticate/', views.must_authenticate_view, name='must_authenticate'),
    path('account/', views.account_view, name='account'),
]
