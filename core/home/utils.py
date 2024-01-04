from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


def send_email_to_user():
    subject = "Test email from django server"
    message = "Test body from django server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['Phourxx0001@gmail.com']
    email_template = render_to_string(template_name="home/email_login.html")
    send_mail(subject=subject, message=message,
              from_email=from_email, recipient_list=recipient_list, fail_silently=False, html_message=email_template)


def send_email_with_attachment(file_path):
    subject = "Test email from django server"
    message = "Test body from django server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["deborahogundiya30@gmail.com"]
    email_template = render_to_string(template_name="home/email_login.html")
    mail = EmailMultiAlternatives(subject=subject, body=message,
                                  from_email=from_email, to=recipient_list)
    mail.attach_file(file_path)
    mail.attach_alternative(email_template, "text/html")
    mail.send(fail_silently=False)
