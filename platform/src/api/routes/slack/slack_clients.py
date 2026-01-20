from fastapi import FastAPI
from fastapi.requests import Request
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
import os

from api.routes.slack.endpoints import paths as slack_paths


def generator(app: FastAPI):

    # Baloot Client
    slack_baloot_app = AsyncApp(
        token=os.getenv('SLACK_VIP_BALOOT_BOT_OAUTH_TOKEN'),
        signing_secret=os.getenv('SLACK_VIP_BALOOT_SIGNING_SECRET'),
        name='VIP-Baloot'
    )

    # Inject Slack Endpoints into Slack Apps
    for slack_path in slack_paths:
        slack_path(slack_baloot_app)

    slack_baloot_app_handler = AsyncSlackRequestHandler(slack_baloot_app)

    # print(f"SLACK_BALOOT_APP_DEV_NAME:", os.getenv('SLACK_VIP_BALOOT_BOT_OAUTH_TOKEN'))

    @app.post('/api/slack/baloot')
    async def slack_baloot_app_api_url(request: Request):
        return await slack_baloot_app_handler.handle(request)