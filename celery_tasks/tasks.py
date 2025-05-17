import logging

from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

from accounts.models import User

SEND_MARKET_EMAIL_COUNTDOWN = 600  # countdown value in seconds

logger = logging.getLogger('users')


@shared_task
def send_register_email(email: str) -> None:
    content = f"Hi there, {email}! You registered successfully."
    send_mail('User Register', content, settings.DEFAULT_FROM_EMAIL, [email])


@shared_task
def send_market_email(email: str) -> None:
    content = f"You can create wishes and read other's"
    send_mail('App Possibilities', content, settings.DEFAULT_FROM_EMAIL, [email])


@shared_task
def log_users_count() -> None:
    logger.info('User count: %d', User.objects.all().count())
