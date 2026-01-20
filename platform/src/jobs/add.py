from celery import Celery


def generator(app: Celery):

    @app.task(
        name='jobs.add'
    )
    def add(x: int, y: int) -> int:
        return x + y