from django.urls import path, re_path
from . import views


urlpatterns = [
    path('totp/create/', views.TOTPCreateView.as_view(), name='totp-create'),
    path('api-token-auth/', views.auth_views.obtain_auth_token),
    re_path(r'^totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerfiyView.as_view(), name='totp-login'),
]
