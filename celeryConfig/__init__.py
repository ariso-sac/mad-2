from celery import Celery
from celery.schedules import crontab
from datetime import datetime 

import os

celery = Celery('tasks')
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/1")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/2")

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, print_current_time_job.s(), name='add every 10')


#### Task ####

@celery.task(name="add_num")
def add_together(a, b):
    return a + b

@celery.task()
def print_current_time_job():
    print("START")
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string) 
    print("COMPLETE")


# celery.conf.beat_schedule = {
#  "run-me-every-ten-seconds": {
#  "task": "tasks.farzi",
#  "schedule": 1.0
#  }
# }

# app.conf.beat_schedule = {
#  # Executes every Monday morning at 7:30 a.m.
#  ‘add-every-monday-morning’: {
#  ‘task’: ‘tasks.add’,
#  ‘schedule’: crontab(hour=7, minute=30, day_of_week=1),
#  ‘args’: (16, 16),
#  },
# }