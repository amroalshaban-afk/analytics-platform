from slack_bolt.async_app import AsyncApp

from services.tasks import app as celery_app

def generator(app: AsyncApp):

    @app.command('/hello')
    async def hello(ack, respond, response_url, command):
        await ack()
        celery_app.send_task('jobs.takes_5_seconds', args=(response_url,))
        # celery_app.send_task('jobs.add', args=(1, 4))
        await respond(text="Hello, MOM!", response_type='in_channel')