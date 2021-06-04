from model_2 import Answerer
from telethon import TelegramClient, events
api_id = 3571461
api_hash = '45e60c503fcdb6f9a0fcc572e97fbcb4'
client = TelegramClient('anon', api_id, api_hash)
# to_whome = ["Totoro", "Looooolllжоржеттта!!!!"]
to_whome = [204658931, 291115490]
answerer = Answerer()


@client.on(events.NewMessage(incoming = True))
async def my_event_handler(event):
    #print(event)
    print(event.message.message)
    if event.message.message == "reset":
        answerer.reset_dialog()
        generated_answer = "dialog reset"
    else:
        generated_answer = answerer.generate_response(event.message.message)
    # generated_answer = 'test'
    sender = await event.get_sender()
    #print(sender)
    if sender.id in to_whome:
        await client.send_message(sender, generated_answer)

client.start()
client.run_until_disconnected()
