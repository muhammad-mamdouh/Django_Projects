from django.core.mail import send_mail
from celery import shared_task
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def deliver_mail_task():
    sleep(5)
    send_mail(
        'Celery Task Scheduler Worked!',
        'This is the body of the mail',
        'mahammad.mamdouh@gmail.com',         # From Address
        ['mahammad.mamdouh@hotmail.com'],     # To Address
    )
    return None
