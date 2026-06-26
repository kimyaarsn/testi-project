from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


def build_absolute_link(path: str) -> str:
    return f"http://127.0.0.1:8000{path}"


def send_activation_email(user):

    activation_path = reverse(
        'active-account',
        kwargs={'code': user.email_active_code}
    )

    activation_link = build_absolute_link(activation_path)

    subject = "فعال‌سازی حساب کاربری"

    message = f"""
سلام {user.username}

برای فعال‌سازی حساب کاربری روی لینک زیر کلیک کنید:

   {activation_link}
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False
    )


def send_reset_password_email(user):

    reset_path = reverse(
        'reset-password',   # یا هر اسمی که در urls.py گذاشته‌ای
        kwargs={
            'code': user.password_reset_code
        }
    )

    reset_link = build_absolute_link(reset_path)

    subject = "بازیابی رمز عبور"

    message = f"""
سلام {user.username}

برای تغییر رمز عبور روی لینک زیر کلیک کنید:

{reset_link}
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False
    )