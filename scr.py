import traceback , asyncio , threading , concurrent.futures , time , random , requests , json , re
from pyrogram import Client,filters
from pathlib import Path
from FUNC.defs import *
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
from FUNC.scraperfunc import *
plugins = dict(root="bot")

user = Client("scrapper",
              api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]) ,
              api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]) )

bot = Client("my_bot",
             api_id = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[0]) ,
             api_hash = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[1]) ,
             bot_token = str(open('FILES/config.txt',encoding="UTF-8").read().splitlines()[2]) ,
             plugins = plugins)

@bot.on_message(filters.command("scr", [".","/"]))
def multi1(Client, message):
    t1 = threading.Thread(target=bcall1, args=(Client, message))
    t1.start()


def bcall1(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(thread1(Client, message))
    loop.close()


async def thread1(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        checkall = check_all_thing(user_id, chat_id, chat_type)
        if checkall[0]==None:
            await message.reply_text(checkall[1], message.id)
        elif checkall[0] == True:
            await message.reply_text(checkall[1], message.id)
        else:
            role = checkall[1]
            try:
                channel_link = message.text.split(" ")[1]
                limit = int(message.text.split(" ")[2])
            except:
                channel_link = None
                limit = None
            if channel_link == None or limit == None:
                resp = f"""<b>
Wrong Format ❌

Usage:
For Public Group Scraping
<code>/scr username 50</code>

For Private Group Scraping
<code>/scr https://t.me/+HLDMU6ZUulY4YmY9 50</code>
            </b>"""
                await message.reply_text(resp, message.id)
            elif role == 'FREE' and int(limit) > 5000:
                resp = """<b>
Limit Reached ⚠️

Message: Your Can Scrape 5000 CC at a Time . Buy Plan to Increase Your Limit .

Type /buy For Paid Plan
</b>"""
                await message.reply_text(resp, message.id)

            elif role == 'PREMIUM' and int(limit) > 10000:
                resp = f"""<b>
Limit Reached ⚠️

Message: Your Can Scrape 10000 CC at a Time .

Type /buy For Paid Plan
</b>"""
                await message.reply_text(resp, message.id)
            else:
                try:
                    await user.start()
                except Exception as e:
                    with open("scraper_logs.txt", "a") as f:
                        f.write(f"{e}\n")
                if "https" in channel_link:
                    check_link = await check_invite_link(user , channel_link)
                    if check_link == False:
                        resp = f"""<b>
Wrong Invite Link ❌

Message: Your Provided Link is Wrong . Please Check Your Link and Try Again .

</b>"""
                        await message.reply_text(resp, message.id)
                    else:
                        channel_id = check_link[1]
                        channel_title = check_link[2]
                        await cc_private_scrape(message , user , bot , channel_id ,channel_title , limit  , role)
                       
                else:
                    resp = f"""<b>
Gate: CC Scraper ✅
 
Message: Scraping {limit} CC From @{channel_link} . Please Wait . 

Status: Scraping...
               </b> """
                    delete = await message.reply_text(resp, message.id)
                    await cc_public_scrape(message , user , bot , channel_link , limit , delete , role)
                    
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")




@bot.on_message(filters.command("scrsk", [".","/"]))
def multi2(Client, message):
    t1 = threading.Thread(target=bcall2, args=(Client, message))
    t1.start()


def bcall2(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(thread2(Client, message))
    loop.close()


async def thread2(Client, message):
    try:
        await user.start()
    except Exception as e:
        with open("scraper_logs.txt", "a") as f:
            f.write(f"{e}\n")
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        checkall = check_all_thing(user_id, chat_id, chat_type)
        if checkall[0]==None:
            await message.reply_text(checkall[1], message.id)
        elif checkall[0] == True:
            await message.reply_text(checkall[1], message.id)
        else:
            role = checkall[1]
            try:
                channel_link = message.text.split(" ")[1]
                limit = int(message.text.split(" ")[2])
            except:
                channel_link = None
                limit = None
            if channel_link == None or limit == None:
                resp = f"""
𝗪𝗿𝗼𝗻𝗴 𝗙𝗼𝗿𝗺𝗮𝘁 ❌

𝗨𝘀𝗮𝗴𝗲:
𝗙𝗼𝗿 𝗣𝘂𝗯𝗹𝗶𝗰 𝗚𝗿𝗼𝘂𝗽 𝗦𝗰𝗿𝗮𝗽𝗽𝗶𝗻𝗴
<code>/scrsk username 50</code>

𝗙𝗼𝗿 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗚𝗿𝗼𝘂𝗽 𝗦𝗰𝗿𝗮𝗽𝗽𝗶𝗻𝗴
<code>/scrsk https://t.me/+HLDMU6ZUulY4YmY9 50</code>
            """
                await message.reply_text(resp, message.id)
            elif role == 'FREE' and int(limit) > 5000:
                resp = f"""
𝗙𝗥𝗘𝗘 𝗨𝗦𝗘𝗥 𝗔𝗥𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗢 5000 𝗦𝗖𝗥𝗔𝗣𝗜𝗡𝗚 𝗟𝗜𝗠𝗜𝗧 ❌
                """
                await message.reply_text(resp, message.id)

            elif role == 'PREMIUM' and int(limit) > 10000:
                resp = f"""
𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗨𝗦𝗘𝗥 𝗔𝗥𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗢 10000 𝗦𝗖𝗥𝗔𝗣𝗜𝗡𝗚 𝗟𝗜𝗠𝗜𝗧 ❌
                """
                await message.reply_text(resp, message.id)
            else:
                try:
                    await user.start()
                except Exception as e:
                    with open("scraper_logs.txt", "a") as f:
                        f.write(f"{e}\n")
                if "https" in channel_link:
                    check_link = await check_invite_link(user , channel_link)
                    if check_link == False:
                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗜𝗻𝘃𝗶𝘁𝗲 𝗟𝗶𝗻𝗸 ❌"
                        await message.reply_text(resp, message.id)
                    else:
                        channel_id = check_link[1]
                        channel_title = check_link[2]
                        await sk_private_scrape(message , user , bot , channel_id ,channel_title , limit  , role)
                else:
                    delete = await message.reply_text("𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝗪𝗮𝗶𝘁...", message.id)
                    await sk_public_scrape(message , user , bot , channel_link , limit , delete , role)
                    
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")



@bot.on_message(filters.command("scrbin", [".","/"]))
def multi3(Client, message):
    t1 = threading.Thread(target=bcall3, args=(Client, message))
    t1.start()


def bcall3(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(thread3(Client, message))
    loop.close()


async def thread3(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        checkall = check_all_thing(user_id, chat_id, chat_type)
        if checkall[0]==None:
            await message.reply_text(checkall[1], message.id)
        elif checkall[0] == True:
            await message.reply_text(checkall[1], message.id)
        else:
            role = checkall[1]
            try:
                scrape_bin = message.text.split(" ")[1]
                channel_link = message.text.split(" ")[2]
                limit = int(message.text.split(" ")[3])
            except:
                scrape_bin = message.text.split(" ")[1]
                channel_link = None
                limit = None
            if channel_link == None or limit == None or scrape_bin == None:
                resp = f"""
𝗪𝗿𝗼𝗻𝗴 𝗙𝗼𝗿𝗺𝗮𝘁 ❌

𝗨𝘀𝗮𝗴𝗲:
𝗙𝗼𝗿 𝗣𝘂𝗯𝗹𝗶𝗰 𝗚𝗿𝗼𝘂𝗽 𝗦𝗰𝗿𝗮𝗽𝗽𝗶𝗻𝗴
<code>/scrbin 443098 username 50</code>

𝗙𝗼𝗿 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗚𝗿𝗼𝘂𝗽 𝗦𝗰𝗿𝗮𝗽𝗽𝗶𝗻𝗴
<code>/scrbin 443098 https://t.me/+HLDMU6ZUulY4YmY9 50</code>
            """
                await message.reply_text(resp, message.id)
            elif role == 'FREE' and int(limit) > 5000:
                resp = f"""
𝗙𝗥𝗘𝗘 𝗨𝗦𝗘𝗥 𝗔𝗥𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗢 5000 𝗦𝗖𝗥𝗔𝗣𝗜𝗡𝗚 𝗟𝗜𝗠𝗜𝗧 ❌
                """
                await message.reply_text(resp, message.id)

            elif role == 'PREMIUM' and int(limit) > 10000:
                resp = f"""
𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗨𝗦𝗘𝗥 𝗔𝗥𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗢 10000 𝗦𝗖𝗥𝗔𝗣𝗜𝗡𝗚 𝗟𝗜𝗠𝗜𝗧 ❌
                """
                await message.reply_text(resp, message.id)
            else:
                try:
                    await user.start()
                except Exception as e:
                    with open("scraper_logs.txt", "a") as f:
                        f.write(f"{e}\n")
                if "https" in channel_link:
                    check_link = await check_invite_link(user , channel_link)
                    if check_link == False:
                        resp = "𝗪𝗿𝗼𝗻𝗴 𝗜𝗻𝘃𝗶𝘁𝗲 𝗟𝗶𝗻𝗸 ❌"
                        await message.reply_text(resp, message.id)
                    else:
                        channel_id = check_link[1]
                        channel_title = check_link[2]
                        await bin_private_scrape(message , user , bot, scrape_bin , channel_id ,channel_title , limit  , role)
                else:
                    delete = await message.reply_text("𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝗪𝗮𝗶𝘁...", message.id)
                    await bin_public_scrape(message , user , bot,  scrape_bin, channel_link , limit , delete , role)
                    
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")