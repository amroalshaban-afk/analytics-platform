from slack_bolt.async_app import AsyncApp
from settings import ENVIRONMENT


def append_app(app: AsyncApp):
    return '-' + app.name.lower() + (ENVIRONMENT if ENVIRONMENT == 'dev' else '')
