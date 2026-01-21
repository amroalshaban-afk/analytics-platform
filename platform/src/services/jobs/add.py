from celery import Celery
import httpx
import asyncio
import time


def generator(app: Celery):

    @app.task(
        name='jobs.add'
    )
    def add(x: int, y: int) -> int:
        return x + y
    

    @app.task(
        name='jobs.takes_5_seconds'
    )
    def takes_5_seconds(response_url):
        time.sleep(5)

        with httpx.Client() as client:
            response = client.post(
                response_url,
                json={
                    "text": "HELLO! THIS IS FROM CELERY.",
                    "response_type": "in_channel"
                }
            )

        return response