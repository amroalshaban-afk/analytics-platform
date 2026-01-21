from celery import Celery
from services.jobs.endpoints import paths as jobs_paths
import os

app = Celery(
    'tasks',
    broker=os.getenv("CELERY_BROKER"),
    # backend=os.getenv("CELERY_RESULT_BACKEND"),
    backend=f"db+psycopg2+{os.getenv('CELERY_RESULT_BACKEND')}"
)

app.conf.database_table_names = {
    'task': 'celery_taskmeta',
    'group': 'celery_tasksetmeta',
}

for jobs_path in jobs_paths:
    jobs_path(app)
