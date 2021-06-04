import asyncio
from telethon import TelegramClient, events, sync
from telethon import utils

# Remember to use your own values from my.telegramА.org!
api_id = 3571461
api_hash = '45e60c503fcdb6f9a0fcc572e97fbcb4'
client = TelegramClient('anon', api_id, api_hash)
#loop = asyncio.get_event_loop()
#client.start()
@client.on(events.NewMessage(chats=('Alexander')))
async def normal_handler(event):
async with client.conversation(event) as conv:
    await conv.send_message('Hey, what is your name?')

    response = await conv.get_response()
    name = response.text

    await conv.send_message('Nice to meet you, {}!'.format(name))





client.run_until_disconnected()