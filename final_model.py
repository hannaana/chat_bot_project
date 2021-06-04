from dialo_gpt_large import Answerer
from telethon import TelegramClient, events
api_id = ******
api_hash = '18c60c5035fcbdb7f9a0fvc132e89fbcv4'
client = TelegramClient('anon', api_id, api_hash)
# to_whome = "User1", "User2" chat id with whom you want to communicate while session
to_whome = [224657931, 251115480]
#pretrained model
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
