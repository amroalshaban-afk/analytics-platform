from api.routes.slack.slash_commands.endpoints import endpoints as slash_commands_paths
from api.routes.slack.events.endpoints import paths as events_paths

paths = [
    *slash_commands_paths,
    *events_paths,
]

