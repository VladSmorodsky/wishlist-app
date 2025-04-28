# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from celery_tasks.celery import app as wishlist_app

__all__ = ('wishlist_app',)