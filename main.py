import os
import traceback
from pyrogram import Client, enums

plugins = dict(root="bot")

# Create the client, we'll name it "user". This is where we'll use the session string.
user = Client(
    "scrapper",
    api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]),
    api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]),
    session_string = os.environ.get('PYROGRAM_SESSION_STRING')  # Get session string from environment variable
)

bot = Client(
    "my_bot",
    api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]),
    api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]),
    bot_token = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[2]),
    plugins = plugins
)

bot.set_parse_mode(enums.ParseMode.HTML)

#IMPORTING SCRAPPER 
from scr import *

print("Done Bot Active ✅")
print("NOW START BOT ONCE MY MASTER")

bot.run()
