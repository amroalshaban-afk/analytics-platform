from fastapi import FastAPI
from fastapi.requests import Request
from slack_bolt.async_app import AsyncApp, AsyncAssistant
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from settings import (
    SLACK_VIP_BALOOT_BOT_OAUTH_TOKEN,
    SLACK_VIP_BALOOT_SIGNING_SECRET,
    SLACK_AWAD_DELIVERY_BOT_OAUTH_TOKEN,
    SLACK_AWAD_DELIVERY_SIGNING_SECRET
)
from api.routes.slack.endpoints import paths as slack_paths
from api.routes.slack.assistants.endpoints import paths as slack_assistant_paths
from utils.slack.context_store import AsyncPostgresAssistantContextStore
from initialize_dbs import operations


def generator(app: FastAPI):
    
    # Slack Clients
    slack_vip_baloot_app = AsyncApp(
        token=SLACK_VIP_BALOOT_BOT_OAUTH_TOKEN,
        signing_secret=SLACK_VIP_BALOOT_SIGNING_SECRET,
        name='VIP-Baloot'
    )
    slack_awad_delivery_app = AsyncApp(
        token=SLACK_AWAD_DELIVERY_BOT_OAUTH_TOKEN,
        signing_secret=SLACK_AWAD_DELIVERY_SIGNING_SECRET,
        name='Awad-Delivery',
    )

    # Slack Assistants
    slack_vip_baloot_assistant = AsyncAssistant(
        app_name='VIP-Baloot',
        thread_context_store=AsyncPostgresAssistantContextStore(db=operations),
    )
    slack_awad_delivery_assistant = AsyncAssistant(
        app_name='Awad-Delivery',
        thread_context_store=AsyncPostgresAssistantContextStore(db=operations),
    )

    # Inject Slack Assistant Endpoints into Slack Apps
    for slack_assistant_path in slack_assistant_paths:
        slack_assistant_path(slack_vip_baloot_assistant)
        slack_assistant_path(slack_awad_delivery_assistant)


    # Attach Assistants to Slack Apps
    slack_vip_baloot_app.use(slack_vip_baloot_assistant)
    slack_awad_delivery_app.use(slack_awad_delivery_assistant)


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
