from slack_bolt.async_app import AsyncAssistant



def generator(assistant: AsyncAssistant):

    # VIP-Baloot
    if assistant.app_name == 'VIP-Baloot':
        ...


    # Awad-Delivery
    if assistant.app_name == 'Awad-Delivery':
        @assistant.thread_started
        async def slack_awad_delivery_assistant_thread_started(payload, set_suggested_prompts, say):
            await set_suggested_prompts(
                prompts=[
                    "Hello!",
                    "Trivia..."
                ]
            )

            await say(text="Hi! How can I help you today?")

