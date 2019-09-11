from django.http import HttpResponse
from .tasks import sleepy, deliver_mail_task


def index(request):
    sleepy.delay(5)
    return HttpResponse('<h1>Done!</h1>')


def deliver_mail(request):
    deliver_mail_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN DELIVERED!</h1>')
