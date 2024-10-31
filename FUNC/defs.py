import traceback
def get_bin_details(cc):
    try:
        import requests
        fbin = cc[:6]
        bin = requests.get(f"https://lookup.binlist.net/{fbin}").json()
        try:
            brand = bin["scheme"].upper()
        except:
            brand = "N/A"
        try:
            type = bin["type"].upper()
        except:
            type = "N/A"
        try:
            level = bin["brand"].upper()
        except:
            level = "N/A"
        try:
            bank_data = bin["bank"]
        except:
            bank_data = "N/A"
        try:
            bank = bank_data["name"].upper()
        except:
            bank = "N/A"
        try:
            country_data = bin["country"]
        except:
            country_data = "N/A"
        try:
            country = country_data["name"].upper()
        except:
            country = "N/A"
        try:
            flag = country_data["emoji"]
        except:
            flag = "N/A"
        try:
            currency = country_data["currency"].upper()
        except:
            currency = "N/A"
        return brand , type , level , bank , country , flag , currency
        
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return "N/A" , "N/A" , "N/A" , "N/A" , "N/A" , "N/A" , "N/A"
def clean(string):
    import re
    text = re.sub("\r|\n", " ", string)
    str1 = re.sub('\s+', ' ', text)
    str = re.sub("[^0-9]", " ", str1)
    string = str.strip()
    lista = re.sub('\s+', ' ', string)
    return lista
    
def multiexplode(string):
    delimiters = [":", "/", " ", "|"]
    one = string
    for delimiter in delimiters:
        one = one.replace(delimiter, delimiters[0])
    two = one.split(delimiters[0])
    return two

def getmessage(message):
    try:
        try:
            msg = message.reply_to_message.text
        except:
            msg = message.text
        validate_msg = getcards(msg)
        if validate_msg != None:
            return validate_msg
        else:
            return False
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return False
    
def getcards(lista):
    try:
        lista = clean(lista)
        len_cc = len(lista)
        chem = lista[0]
        cc, mes, ano, cvv = multiexplode(lista)[:4]
        len_cc = len(cc)
        len_mes = len(mes)
        ano1 = ano
        vaut = [1, 2, 7, 8, 9, 0]
        if chem in vaut:
            return
        if not lista:
            return
        if len_cc < 15:
            return
        if len_mes > 2:
            ano = cvv
            cvv = mes
            mes = ano1
        return cc, mes, ano, cvv
    except Exception as e:
        return
    
def check_stripe(sk):
    try:
        import stripe
        stripe.api_key = sk
        pm = stripe.Token.create(
        card={
            "number": "4100390462423118",
            "exp_month": "09",
            "exp_year": "30",
            "cvc": "100"
        },
        )
        result = "LIVE"
    except Exception as e:
        result = str(e)
    if result == "LIVE":
        return True
    elif "rate limit" in result:
        return True
    elif "Invalid API Key" in result:
        return False
    elif "Expired API Key provided" in result:
        return False
    elif "Your account cannot currently make live charges." in result:
        return False
    else:
        return False


def brodcast_msg(msg , user_id):
    import urllib.parse
    msg = urllib.parse.quote_plus(msg)
    try:
        import requests
        send = requests.get(f"https://api.telegram.org/bot{open('FILES/config.txt', encoding='UTF-8').read().splitlines()[2]}/sendMessage?chat_id={user_id}&text={msg}&parse_mode=HTML&disable_web_page_preview=True")
        if "true" in send.text:
            return True
        else:
            return False
    except:
        return False


def getallsk():
    try:
        sks = []
        with open('FILES/sk.txt', 'r') as file:
            sks = [line.strip() for line in file.readlines()]

        if len(sks) == 0:
            return ["sk_live_E8nn7DSL0YVxp8pFDUIfOujj"]
        else:
            return sks
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")


def getsk():
    try:
        import random
        sks = getallsk()
        try:
            sk = random.choice(sks)
        except:
            sk = "sk_live_SAKURATHESK"
        return sk
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")





