from utils.slack_helpers import append_app
from slack_bolt.async_app import AsyncApp
# from services.tasks import app as celery_app
import asyncio

def generator(app: AsyncApp):

    if app.name in ('VIP-Baloot', 'Awad-Delivery'):
        @app.command(f'/hello{append_app(app)}')
        async def hello(ack, respond, payload, response_url, command):
            await ack()
            print(payload)
            await respond(text="Hello, MOM!", response_type='in_channel')
        
        @app.event('app_mention')
        async def testing_app_mentions(ack, payload, client):
            await ack()
            print(payload)
            conversations = await client.conversations_replies(
                channel=payload['channel'],
                ts='1769174306.233399'
            )
            await asyncio.sleep(5)
            # await say(text='Hello, thank you for mentioning me!')
            await client.chat_postMessage(
                channel=payload['channel'],
                thread_ts=payload['ts'],
                text='Reply in thread'
            )
        
        @app.event('message')
        async def testing_app_message(ack, payload):
            await ack()
            print(payload)