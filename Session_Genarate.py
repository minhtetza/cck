import traceback
from pyrogram import Client

user = Client("scrapper",
              api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]) ,
              api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]) )


user.start()