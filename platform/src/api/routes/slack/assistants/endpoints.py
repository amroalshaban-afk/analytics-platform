from api.routes.slack.assistants.use_message import generator as use_message
from api.routes.slack.assistants.thread_started import generator as thread_started
from api.routes.slack.assistants.thread_context_changed import generator as thread_context_changed


paths = [
    use_message,
    thread_started,
    thread_context_changed,
]