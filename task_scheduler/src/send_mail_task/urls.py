from django.urls import path
from . import views


app_name    = 'mail_task'
urlpatterns = [
    path('', views.index, name='index'),
    path('mail/', views.deliver_mail, name='mail'),
]
