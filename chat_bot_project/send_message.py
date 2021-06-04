from telethon import TelegramClient, events, sync
from telethon import utils

# Remember to use your own values from my.telegram.org!
api_id = 3571461
api_hash = '45e60c503fcdb6f9a0fcc572e97fbcb4'
client = TelegramClient('anon', api_id, api_hash)

client.start()

destination_user_username='Looooolllжоржеттта!!!!'

entity=client.get_entity(destination_user_username)
client.send_message(entity=entity, message="худенький це не дуже добре ор(")





client.run_until_disconnected()





