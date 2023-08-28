# 1. pip3 install telethon
# 2. Go to https://my.telegram.org/ and get api_id, api_hash

from telethon import TelegramClient, events, sync
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

api_id = 12345
api_hash = 'PUT-YOUR-API-HASH-HERE'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
async def my_event_handler(event):
    #is_from_someone = event.message.from_id == 123456789
    is_media = event.message.media != None and event.message.document != None 
    is_sticker = is_media and (event.message.document.mime_type == "image/webp" or event.message.document.mime_type == "application/x-tgsticker")
    is_gif = is_media and event.message.document.mime_type == "video/mp4" and event.message.document.size < 1024 * 1024
    if is_sticker or is_gif:
        await event.delete()

me = client.get_me()
print(me.stringify())
	
with client:
    client.run_until_disconnected()
