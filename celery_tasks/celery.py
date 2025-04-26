import os
from datetime import timedelta

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist.settings')

app = Celery('wishlist')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(['celery_tasks.tasks'])

app.conf.beat_schedule = {
    'log_users_count': {
        'task': 'celery_tasks.tasks.log_users_count',
        'schedule': timedelta(seconds=10),
    }
}