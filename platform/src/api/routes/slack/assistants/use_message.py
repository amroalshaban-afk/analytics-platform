from slack_bolt.async_app import AsyncAssistant
import os
import asyncio


def generator(assistant: AsyncAssistant):

    # VIP-Baloot
    if assistant.app_name == 'VIP-Baloot':

        @assistant.user_message
        async def slack_vip_baloot_assistant_user_message(payload, set_status, client):
            # print(payload)
            user_id = payload['user']
            channel_id = payload['channel']
            thread_ts = payload['thread_ts']

            await set_status(
                status='Thinking...',
                loading_messages=[
                    "This is the first thinking message...",
                    "This is the second thinking message...",
                    "This is the third thinking message...",
                ]
            )

            await asyncio.sleep(5)
            random_response = """It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well. Above are a few examples of how the random paragraph generator can be beneficial. The best way to see if this random paragraph picker will be useful for your intended purposes is to give it a try. Generate a number of paragraphs to see if they are beneficial to your current project. If you do find this paragraph tool useful, please do us a favor and let us know how you're using it. It's greatly beneficial for us to know the different ways this tool is being used so we can improve it with updates. This is especially true since there are times when the generators we create get used in completely unanticipated ways from when we initially created them. If you have the time, please send us a quick note on what you'd like to see changed or added to make it better in the future."""
            chunks = [letter for letter in random_response]

            streamer = await client.chat_stream(channel=channel_id, thread_ts=thread_ts)
            print(dir(streamer))
            for chunk in chunks:
                await streamer.append(markdown_text=chunk)

            await streamer.stop()


    # Awad-Delivery
    if assistant.app_name == 'Awad-Delivery':

        @assistant.user_message
        async def slack_vip_baloot_assistant_user_message(payload, set_status, client):
            # print(payload)
            user_id = payload['user']
            channel_id = payload['channel']
            thread_ts = payload['thread_ts']

            await set_status(
                status='Thinking...',
                loading_messages=[
                    "This is the first thinking message...",
                    "This is the second thinking message...",
                    "This is the third thinking message...",
                ]
            )

            await asyncio.sleep(5)
            random_response = """King of delivery - Awad Abu Shafa

Awad Abu Shafa, the leader of the region, is taking over the service to serve his friend Jabr Qawans in a unique 3D toy. Awad Abu Shifa is a seasoned driver who drives time and loves the streets of Amman.

Choose your car, modify it, and develop it throughout Amman and its environs

Collect orders from restaurants and connect them to the right place before the time is up
Develop your car and discover multiple new restaurants

Game features:
- Unique 3D drawings
Funny characters
- Multiple cars are scalable
- Large map and open world

Do not forget to evaluate the game and admire our page on Facebook, this game comes from Tomato, the publisher of the first Arab games on mobile devices in the Arab world

King of delivery - Awad abo shefeh

Awad abu sheffeh is a skilled driver who keeps his friend Jaber Gawanes to deliver food in a new 3D one of a kind car game.

Take a ride in Awad's car around the city of Amman and collect orders from restaurants and deliver it to the right place before the time run out

Upgrade your car and unlock multiple restaurants to make more & more deliveries!

The game features:
1 - Unique 3D Graphics
2 - Funny characters
3 - Multiple up-gradable cars
4 - Large map and open world"""
            chunks = [letter for letter in random_response]

            streamer = await client.chat_stream(channel=channel_id, thread_ts=thread_ts)
            print(dir(streamer))
            for chunk in chunks:
                await streamer.append(markdown_text=chunk)

            await streamer.stop()