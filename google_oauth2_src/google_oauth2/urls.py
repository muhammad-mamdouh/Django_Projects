from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignInView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),

    path('oauth/', include('social_django.urls', namespace='social')),
]
