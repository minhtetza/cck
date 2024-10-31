import traceback
import requests , random , json , time
from FUNC.defs import getsk 
def create_charge(fullcc , sks , session):
    try:
        sk = random.choice(sks)
        splitter = fullcc.split("|")
        cc = splitter[0]
        mes = splitter[1]
        ano = splitter[2]
        while True:
            url1 = "https://api.stripe.com/v1/payment_methods"
            headers1 = {
                "Authorization": f"Bearer {sk}",
            }
            data1 = f"type=card&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}"
            result1 = session.post(url1, headers=headers1, data=data1)
            if "rate_limit" in result1.text:
                continue
            else:
                break
        try:
            id = result1.json()["id"]
        except:
            return result1.text
        while True:
            url2 = "https://api.stripe.com/v1/payment_intents"
            headers2 = {
                "Authorization": f"Bearer {sk}",
            }
            data2 = f"amount=100&currency=usd&payment_method_types[]=card&payment_method={id}&confirm=true&off_session=true&description=FoxDonation"
            result2 = session.post(url2, headers=headers2, data=data2)
            if "rate_limit" in result2.text:
                continue
            else:
                break
        return result2.text

    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")
        return str(e)
    
    