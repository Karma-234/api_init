from django.core.mail import send_mail
from django.conf import settings


def send_email_to_user():
    subject = "Test email"
    message = "TEset body"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['kamal@propaddy.com']
    send_mail(subject=subject, message=message,
              from_email=from_email, recipient_list=recipient_list, fail_silently=False)
