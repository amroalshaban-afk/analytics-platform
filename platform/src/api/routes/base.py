from fastapi import FastAPI
from utils.func1 import add

from services.tasks import app as celery_app


def generator(app: FastAPI):

    @app.get('/')
    async def endpoint1():
        return {"endpoint1": f"Hello, MOM! {add(1, 1)}"}