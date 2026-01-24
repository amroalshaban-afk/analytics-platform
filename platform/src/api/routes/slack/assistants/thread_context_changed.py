from slack_bolt.async_app import AsyncAssistant


def generator(assistant: AsyncAssistant):

    # VIP-Baloot
    if assistant.app_name == 'VIP-Baloot':
        ...


    # Awad-Delivery
    if assistant.app_name == 'Awad-Delivery':

        @assistant.thread_context_changed
        async def slack_awad_delivery_assistant_thread_context_changed(payload, get_thread_context, save_thread_context):

            await save_thread_context(new_context={
                    'user_id': payload['assistant_thread']['user_id'],
                    'team_id': payload['assistant_thread']['context']['team_id'],
                    'context': payload['assistant_thread']['context'],
                    'payload': payload,
                }
            )
