from celery import Celery
from jobs.endpoints import paths as jobs_paths


app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//'
)

for jobs_path in jobs_paths:
    jobs_path(app)
