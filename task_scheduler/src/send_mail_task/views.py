from django.http import HttpResponse
from .tasks import sleepy


def index(request):
    sleepy.delay(5)
    return HttpResponse('<h1>Done!</h1>')
