from fastapi import FastAPI
from fastapi.requests import Request
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
import os

from api.routes.slack.endpoints import paths as slack_paths


def generator(app: FastAPI):

    # Slack Clients
    slack_vip_baloot_app = AsyncApp(
        token=os.getenv('SLACK_VIP_BALOOT_BOT_OAUTH_TOKEN'),
        signing_secret=os.getenv('SLACK_VIP_BALOOT_SIGNING_SECRET'),
        name='VIP-Baloot'
    )
    slack_awad_delivery_app = AsyncApp(
        token=os.getenv('SLACK_AWAD_DELIVERY_BOT_OAUTH_TOKEN'),
        signing_secret=os.getenv('SLACK_AWAD_DELIVERY_SIGNING_SECRET'),
        name='Awad-Delivery',
    )


    # Inject Slack Endpoints into Slack Apps
    for slack_path in slack_paths:
        slack_path(slack_vip_baloot_app)
        slack_path(slack_awad_delivery_app)


    # Define Slack App Handlers
    slack_vip_baloot_app_handler = AsyncSlackRequestHandler(slack_vip_baloot_app)
    slack_awad_delivery_app_handler = AsyncSlackRequestHandler(slack_awad_delivery_app)


    # Define Slack App POST Endpoints
    @app.post('/api/slack/vip-baloot')
    async def slack_vip_baloot_app_api_url(request: Request):
        return await slack_vip_baloot_app_handler.handle(request)
    
    @app.post('/api/slack/awad-delivery')
    async def slack_awad_delivery_app_api_url(request: Request):
        return await slack_awad_delivery_app_handler.handle(request)
