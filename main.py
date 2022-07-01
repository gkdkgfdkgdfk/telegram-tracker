# -*- coding: utf-8 -*-
from telethon import TelegramClient, sync, events
from datetime import *

api_id = 15302040
api_hash = 'e750b9e72dbeee1ab7c0f78526a44417'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.UserUpdate(chats=ID человека))
async def handler(event):
    if event.online:
        my_file = open("logs.txt", "a+")
        my_file.write("\n[" + str(datetime.now()) + "] User online")
        my_file.close()

client.start()
client.run_until_disconnected()
