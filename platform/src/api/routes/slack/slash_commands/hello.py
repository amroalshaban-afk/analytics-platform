from slack_bolt.async_app import AsyncApp


def generator(app: AsyncApp):

    @app.command('/hello')
    async def hello(ack, respond, command):
        await ack()
        await respond(text="Hello, MOM!", response_type='in_channel')