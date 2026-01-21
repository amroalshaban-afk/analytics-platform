from slack_bolt.async_app import AsyncApp
# from services.tasks import app as celery_app


def generator(app: AsyncApp):

    if app.name in ('VIP-Baloot', 'Awad-Delivery'):
        @app.command(f'/hello-{app.name.lower()}')
        async def hello(ack, respond, response_url, command):
            await ack()
            await respond(text="Hello, MOM!", response_type='in_channel')