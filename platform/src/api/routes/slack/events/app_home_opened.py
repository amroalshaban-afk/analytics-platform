from slack_bolt.async_app import AsyncApp


def generator(app: AsyncApp):

    @app.event('app_home_opened')
    async def app_home_opened(payload, ack, client):
        await ack()

        user_id = payload['user']
        user_info = await client.users_info(user=user_id)

        await client.views_publish(
            user_id=user_id,
            view={
                "type": "home",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"Hello, {user_info['user']['real_name']}!"
                        }
                    },
                    {
                        "type": "image",
                        # "image_url": "https://i.ibb.co/dJ4YS4pv/data-wallpaper.jpg",
                        "image_url": user_info['user']['profile']['image_original'],
                        "alt_text": "This is the OKRs"
                    }
                ]
            }
        )