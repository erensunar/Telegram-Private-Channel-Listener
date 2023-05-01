import json
from telethon import TelegramClient,events

f = open('config.json')
data = json.load(f)
phone_number = data["phone number"]
api_id = data["api id"]
api_hash = data["api hash"]
chat_id = data["chat id"]



client = TelegramClient(phone_number, api_id, api_hash)


# Bot hesabınızı kullanarak gizli kanala bağlanın
async def connect_to_channel(channel_username):
    channel = await client.get_entity(channel_username)
    return channel

# Kanala bağlandıktan sonra mesajları alın
@client.on(events.NewMessage(chat_id))
async def my_event_handler(event):
    print("---------------------\n" + event.text + "\n", event.sender_id)


with client:
    # Gizli kanala bağlanın
    print(f"Connect to  {chat_id}..")
    channel = client.loop.run_until_complete(connect_to_channel(chat_id))

    # Kanalda yeni mesajlar olup olmadığını dinleyin
    client.run_until_disconnected()