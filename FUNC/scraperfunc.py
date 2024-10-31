import traceback
from FUNC.defs import *
from pyrogram import Client, enums
from pathlib import Path

async def cc_public_scrape(message , user , bot , channel_link , limit , delete , role):
    try:
        ccs = []
        amt = 0
        dublicate = 0
        async for msg in user.get_chat_history(channel_link, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            ccs.append(getcc)
                            amt += 1

            except:
                getcc = getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In @{channel_link} .

</b>"""
            await message.reply_text(resp, message.id)
        else:
            file_name = f"{limit}x_CC_Scraped_By_@Sakura.txt"
            with open(file_name, 'a' , encoding="UTF-8") as f:
                for x in ccs:
                    cc = x[0]
                    mes = x[1]
                    ano = x[2]
                    cvv = x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            chat_info = await user.get_chat(channel_link)
            title = chat_info.title
            await bot.delete_messages(message.chat.id, delete.id)
            caption = f"""<b>
CC Scraped ✅

● Source: {title}
● Targeted Amount: {limit}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
● {open('FILES/config.txt',encoding="UTF-8").read().splitlines()[3]}</b>
"""
            scr_done = await message.reply_document(
                document=file_name,
                caption=caption,
                reply_to_message_id=message.id)
            if scr_done:
                name = file_name
                my_file = Path(name)
                my_file.unlink(missing_ok=True)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{e}</b>", message.id)

async def check_invite_link(user , channel_link):
    try:
        chat_info = await user.get_chat(channel_link)
        channel_id = chat_info.id
        title = chat_info.title
        return True , channel_id , title
    except:
        try:
            join = await user.join_chat(channel_link)
            title = join.title
            channel_id = join.id
            return True , channel_id , title
        except Exception as e:
            with open("error_logs.txt", "a") as f:
                f.write(f"{e}\n")
            return False
        
async def cc_private_scrape(message , user , bot , channel_id ,channel_title , limit  , role):
    try:
        ccs = []
        amt = 0
        dublicate = 0
        resp = f"""<b>
Gate: CC Scraper ✅

Message: Scraping {limit} CC From {channel_title} . Please Wait . 

Status: Scraping...
            </b> """
        delete = await message.reply_text(resp, message.id)
        async for msg in user.get_chat_history(channel_id, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            ccs.append(getcc)
                            amt += 1

            except:
                getcc = getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In {channel_title} .

</b>"""
            await message.reply_text(resp, message.id)

        else:
            file_name = f"{limit}x_CC_Scraped_By_@Sakura.txt"
            with open(file_name, 'a' , encoding="UTF-8") as f:
                for x in ccs:
                    cc = x[0]
                    mes = x[1]
                    ano = x[2]
                    cvv = x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            await bot.delete_messages(message.chat.id, delete.id)
            caption = f"""<b>
CC Scraped ✅

● Source: {channel_title}
● Targeted Amount: {limit}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
● {open('FILES/config.txt',encoding="UTF-8").read().splitlines()[3]}</b>
"""
            scr_done = await message.reply_document(
                document=file_name,
                caption=caption,
                reply_to_message_id=message.id)
            if scr_done:
                name = file_name
                my_file = Path(name)
                my_file.unlink(missing_ok=True)
            
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{e}</b>", message.id)

                

async def bin_public_scrape(message , user , bot,  scrape_bin, channel_link , limit , delete , role):
    try:
        ccs = []
        amt = 0
        dublicate = 0
        async for msg in user.get_chat_history(channel_link, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            if scrape_bin in getcc[0][:6]:
                                ccs.append(getcc)
                                amt += 1

            except:
                getcc = getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In @{channel_link} .

</b>"""
            await message.reply_text(resp, message.id)
            
        else:
            file_name = f"{limit}x_CC_Scraped_By_@Sakura.txt"
            with open(file_name, 'a' , encoding="UTF-8") as f:
                for x in ccs:
                    cc = x[0]
                    mes = x[1]
                    ano = x[2]
                    cvv = x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            chat_info = await user.get_chat(channel_link)
            title = chat_info.title
            await bot.delete_messages(message.chat.id, delete.id)
            caption = f"""<b>
CC Scraped ✅

● Source: {title}
● Targeted Amount: {limit}
● Targeted Bin: {scrape_bin}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
● {open('FILES/config.txt',encoding="UTF-8").read().splitlines()[3]}</b>
"""
            scr_done = await message.reply_document(
                document=file_name,
                caption=caption,
                reply_to_message_id=message.id)
            if scr_done:
                name = file_name
                my_file = Path(name)
                my_file.unlink(missing_ok=True)
            
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{e}</b>", message.id)
 

async def bin_private_scrape(message , user , bot, scrape_bin , channel_id ,channel_title , limit  , role):
    try:
        ccs = []
        amt = 0
        dublicate = 0
        resp = f"""<b>
Gate: CC Scraper ✅

Message: Scraping {limit} CC From {channel_title} . Please Wait . 

Status: Scraping...
            </b> """
        delete = await message.reply_text(resp, message.id)
        async for msg in user.get_chat_history(channel_id, limit):
            msg = str(msg.text)
            try:
                for x in msg.split("\n"):
                    getcc = getcards(x)
                    if getcc:
                        if getcc in ccs:
                            dublicate += 1
                        else:
                            if scrape_bin in getcc[0][:6]:
                                ccs.append(getcc)
                                amt += 1

            except:
                getcc = getcards(msg)
                if getcc:
                    if getcc in ccs:
                        dublicate += 1
                    else:
                        ccs.append(getcc)
                        amt += 1
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No CC Found ❌

Message: We Didnt Find Any CC In {channel_title} .

</b>"""
            await message.reply_text(resp, message.id)
            
        else:
            file_name = f"{limit}x_CC_Scraped_By_@Sakura.txt"
            with open(file_name, 'a' , encoding="UTF-8") as f:
                for x in ccs:
                    cc = x[0]
                    mes = x[1]
                    ano = x[2]
                    cvv = x[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    f.write(f"{fullcc}\n")
            await bot.delete_messages(message.chat.id, delete.id)
            caption = f"""<b>
CC Scraped ✅

● Source: {channel_title}
● Targeted Amount: {limit}
● Targeted Bin: {scrape_bin}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
● {open('FILES/config.txt',encoding="UTF-8").read().splitlines()[3]}</b>
"""
            scr_done = await message.reply_document(
                document=file_name,
                caption=caption,
                reply_to_message_id=message.id)
            if scr_done:
                name = file_name
                my_file = Path(name)
                my_file.unlink(missing_ok=True)
            
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")

        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{e}</b>", message.id)



async def sk_public_scrape(message , user , bot , channel_link , limit , delete , role):
    try:
        ccs = []
        amt = 0
        dublicate = 0
        async for msg in user.get_chat_history(channel_link, limit):
            msg = str(msg.text)
            if "sk_live" in msg:          
                sk = msg.split("sk_live")[1].split(" ")[0]
                if "xxxxx" in sk:
                    pass
                else:
                    if "\n" in sk:
                        sk = sk.split("\n")[0]
                    if "✅" in sk:
                        sk = sk.splice("✅")[1]
                    sk = "sk_live_" + sk 
                    if sk in ccs:
                        dublicate += 1
                    else:
                        amt += 1
                        ccs.append(sk)
                        
        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No SK Found ❌

Message: We Didnt Find Any SK In @{channel_link} .

</b>"""
            await message.reply_text(resp, message.id)
            
        else:
            file_name = f"{limit}x_SK_Scraped_By_@Sakura.txt"
            with open(file_name, 'a' , encoding="UTF-8") as f:
                for x in ccs:
                    f.write(f"{x}\n")
            chat_info = await user.get_chat(channel_link)
            title = chat_info.title
            await bot.delete_messages(message.chat.id, delete.id)
            caption = f"""<b>
SK Scraped ✅

● Source: {title}
● Targeted Amount: {limit}
● SK Found: {amt}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
● {open('FILES/config.txt',encoding="UTF-8").read().splitlines()[3]}</b>
"""
            scr_done = await message.reply_document(
                document=file_name,
                caption=caption,
                reply_to_message_id=message.id)
            if scr_done:
                name = file_name
                my_file = Path(name)
                my_file.unlink(missing_ok=True)
            
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{e}</b>", message.id)
 
                

async def sk_private_scrape(message , user , bot , channel_id ,channel_title , limit  , role):
    try:
        ccs = []
        amt = 0
        dublicate = 0
        resp = f"""<b>
Gate: SK Scraper ✅

Message: Scraping {limit} SK From {channel_title} . Please Wait . 

Status: Scraping...
            </b> """
        delete = await message.reply_text(resp, message.id)
        async for msg in user.get_chat_history(channel_id, limit):
            msg = str(msg.text)
            if "sk_live" in msg:          
                sk = msg.split("sk_live")[1].split(" ")[0]
                if "xxxxx" in sk:
                    pass
                else:
                    if "\n" in sk:
                        sk = sk.split("\n")[0]
                    if "✅" in sk:
                        sk = sk.splice("✅")[1]
                    sk = "sk_live_" + sk 
                    if sk in ccs:
                        dublicate += 1
                    else:
                        amt += 1
                        ccs.append(sk)

        if amt == 0:
            await bot.delete_messages(message.chat.id, delete.id)
            resp = f"""<b>
No SK Found ❌

Message: We Didnt Find Any SK In {channel_title} .

</b>"""
            await message.reply_text(resp, message.id)
            
        else:
            file_name = f"{limit}x_SK_Scraped_By_@Sakura.txt"
            with open(file_name, 'a' , encoding="UTF-8") as f:
                for x in ccs:
                    f.write(f"{x}\n")
            await bot.delete_messages(message.chat.id, delete.id)
            caption = f"""<b>
SK Scraped ✅

● Source: {channel_title}
● Targeted Amount: {limit}
● CC Found: {amt}
● Duplicate Removed: {dublicate}
● Scraped By: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
● {open('FILES/config.txt',encoding="UTF-8").read().splitlines()[3]}</b>
"""
            scr_done = await message.reply_document(
                document=file_name,
                caption=caption,
                reply_to_message_id=message.id)
            if scr_done:
                name = file_name
                my_file = Path(name)
                my_file.unlink(missing_ok=True)
            
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
        await bot.delete_messages(message.chat.id, delete.id)
        await message.reply_text(f"<b>Error ❌\n\n{e}</b>", message.id)
               