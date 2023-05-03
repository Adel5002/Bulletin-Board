import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MMORPGproj.settings')

app = Celery('MMORPGproj')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.autodiscover_tasks()