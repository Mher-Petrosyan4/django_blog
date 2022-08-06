from django.core.mail import EmailMessage
from django.conf import settings


def send_email(subject, body, recipients):
    mail = EmailMessage(subject=subject, body=body, to=recipients, from_email=settings.EMAIL_HOST_USER)

    mail.send()