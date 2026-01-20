from api.routes.base import generator as base
from api.routes.slack.slack_clients import generator as slack_clients

paths = [
    base,
    slack_clients,
]