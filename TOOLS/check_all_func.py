import traceback
from FUNC.usersdb_func import *
import time
from FUNC.defs import *
def check_all_thing(user_id , chat_id , chat_type ):
    try:
        regdata = str(getuserinfo(user_id))
        if regdata == 'None':
            resp = f"""<b>
❌ 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 ❌

𝖬𝖾𝗌𝗌𝖺𝗀𝖾: 𝖸𝗈𝗎 𝖺𝗋𝖾 𝖺𝗅𝗋𝖾𝖺𝖽𝗒 𝗋𝖾𝗀𝗂𝗌𝗍𝖾𝗋𝖾𝖽 𝗂𝗇 𝗈𝗎𝗋 𝖻𝗈𝗍. 𝖭𝗈 𝗇𝖾𝖾𝖽 𝗍𝗈 𝗋𝖾𝗀𝗂𝗌𝗍𝖾𝗋 𝗇𝗈𝗐.

𝖯𝗅𝖾𝖺𝗌𝖾 𝖱𝖾𝗀𝗂𝗌𝗍𝖾𝗋 𝖧𝖾𝗋𝖾 𝖴𝗌𝗂𝗇𝗀 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 '/register'
</b>"""
            return None , resp
            
        else:
            getuser = getuserinfo(user_id)
            status = getuser["status"]
            plan = getuser["plan"]
            expiry = getuser["expiry"]
            credit = int(getuser["credit"])
            antispam_time = int(getuser["antispam_time"])
            now = int(time.time())
            count_antispam = now - antispam_time
            checkgroup = str(getchatinfo(chat_id))
            plancheck = plan_expirychk(user_id)

            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = f"""<b>
Premium Users Required ⚠️

Message: Only Premium Users are Allowed to use bot in Personal . Although You Can Use Bot Free Here https://t.me/OmenXD_Bins

Buy Premium Plan Using /buy to Continue
</b>"""
                return True , resp 

            elif chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP" and checkgroup == "None":
                resp = f"""<b>
Unauthorized Chats ⚠️

Message: Only Chats Approved By My Master Can Only Use Me . To Get Approved Your Chats Follow The Steps .

Type /howgp to Know The Step
</b>"""
                return True , resp
                
            elif credit < 5:
                resp = f"""<b>
Insufficient Credits ⚠️

Message: You Have Insufficient Credits to Use Me . Recharge Credit For Using Me

Type /buy to Recharge
</b>"""
                return True , resp       
                          
            elif status != 'FREE' and count_antispam < 5:
                after = 5 - count_antispam
                resp = f"""<b>
Antispam Detected ⚠️

Message: You Are Doing things Very Fast . Try After {after}s to Use Me Again .

Reduce Antispam Time /buy Using Paid Plan
</b>"""
                return True , resp
                
            elif count_antispam < 20:
                after = 20 - count_antispam
                resp = f"""<b>
Antispam Detected ⚠️

Message: You Are Doing things Very Fast . Try After {after}s to Use Me Again .

Reduce Antispam Time /buy Using Paid Plan
</b>"""
                return True , resp
            elif plancheck == "YES":
                resp = f"""<b>
Plan Expired ⚠️

Message: Your Current Plan is Expired . To Regain Access Purchase Again Our One Of Plan .

Type /buy To Purchase Plan
</b>"""
                try:
                    import requests
                    requests.get(f"https://api.telegram.org/bot{open('FILES/config.txt', encoding='UTF-8').read().splitlines()[2]}/sendMessage?chat_id={user_id}&text={resp}&parse_mode=HTML")
                except:
                    pass
                return False , status
            else:
                return False , status

               
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
    

def check_some_thing(user_id , chat_id , chat_type ):
    try:
        regdata = str(getuserinfo(user_id))
        if regdata == 'None':
            resp = f"""<b>
❌ 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 ❌

𝖬𝖾𝗌𝗌𝖺𝗀𝖾: 𝖸𝗈𝗎 𝖺𝗋𝖾 𝖺𝗅𝗋𝖾𝖺𝖽𝗒 𝗋𝖾𝗀𝗂𝗌𝗍𝖾𝗋𝖾𝖽 𝗂𝗇 𝗈𝗎𝗋 𝖻𝗈𝗍. 𝖭𝗈 𝗇𝖾𝖾𝖽 𝗍𝗈 𝗋𝖾𝗀𝗂𝗌𝗍𝖾𝗋 𝗇𝗈𝗐.

𝖯𝗅𝖾𝖺𝗌𝖾 𝖱𝖾𝗀𝗂𝗌𝗍𝖾𝗋 𝖧𝖾𝗋𝖾 𝖴𝗌𝗂𝗇𝗀 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 '/register'
</b>"""
            return "None" , resp
            
        else:
            getuser = getuserinfo(user_id)
            status = getuser["status"]
            plan = getuser["plan"]
            expiry = getuser["expiry"]
            credit = int(getuser["credit"])
            antispam_time = int(getuser["antispam_time"])
            now = int(time.time())
            count_antispam = now - antispam_time
            checkgroup = str(getchatinfo(chat_id))
            plancheck = plan_expirychk(user_id)

            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = f"""<b>
Premium Users Required ⚠️

Message: Only Premium Users are Allowed to use bot in Personal . Although You Can Use Bot Free Here https://t.me/OmenXD_Bins

Buy Premium Plan Using /buy to Continue
</b>"""
                return True , resp 

            elif chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP" and checkgroup == "None":
                resp = f"""<b>
Unauthorized Chats ⚠️

Message: Only Chats Approved By My Master Can Only Use Me . To Get Approved Your Chats Follow The Steps .

Type /howgp to Know The Step
</b>"""
                return True , resp
                
            elif plancheck == "YES":
                resp = f"""<b>
Plan Expired ⚠️

Message: Your Current Plan is Expired . To Regain Access Purchase Again Our One Of Plan .

Type /buy To Purchase Plan
</b>"""
                try:
                    import requests
                    requests.get(f"https://api.telegram.org/bot{open('FILES/config.txt', encoding='UTF-8').read().splitlines()[2]}/sendMessage?chat_id={user_id}&text={resp}&parse_mode=HTML")
                except:
                    pass
                return False , status
            else:
                return False , status

               
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")