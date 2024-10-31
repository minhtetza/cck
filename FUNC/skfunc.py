import traceback
def getskinfo(sk):
    import stripe
    stripe.api_key = sk
    all = stripe.radar.ValueList.list()
    useripdb = ""
    cardbindb = ""
    cardcountrydb = ""
    ipcountrydb = ""
    usersipresp = """Users IP Blacklisted: (0)
N/A"""
    cardbinresp = """Card Bin Blacklisted: (0)
N/A"""
    cardcountryresp = """Card Country Blacklisted: (0)
N/A"""
    ipcountryresp = """Country's IP Blacklisted: (0)
N/A"""
    for i in all:
        module = i["alias"]
        if module == "client_ip_address_blocklist":
            totalip = i["list_items"]["total_count"]
            if totalip != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    useripdb += each + "\n"
                usersipresp = f"""Users IP Blacklisted: ({totalip})
{useripdb}"""
            else:
                usersipresp = f"""Users IP Blacklisted: ({totalip})
N/A"""
        elif module == "card_bin_blocklist":
            totalbin = i["list_items"]["total_count"]
            if totalbin != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    cardbindb += each + "\n"
                cardbinresp = f"""Card Bin Blacklisted: ({totalbin})
{cardbindb}"""
            else:
                cardbinresp = f"""Card Bin Blacklisted: ({totalbin})
N/A"""
        elif module == "card_country_blocklist":
            totalcountry = i["list_items"]["total_count"]
            if totalcountry != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    cardcountrydb += each + "\n"
                cardcountryresp = f"""Card Country Blacklisted: ({totalcountry})
{cardcountrydb}"""
            else:
                cardcountryresp = f"""Card Country Blacklisted: ({totalcountry})
N/A"""

        elif module == "client_ip_country_blocklist":
            ipcountry = i["list_items"]["total_count"]
            if ipcountry != 0:
                alldata = i["list_items"]["data"]
                for data in alldata:
                    each = data["value"]
                    ipcountrydb += each + "\n"
                ipcountryresp = f"""Country's IP Blacklisted: ({ipcountry})
{ipcountrydb}"""
            else:
                ipcountryresp = f"""Country's IP Blacklisted: ({ipcountry})
N/A"""
        else:
            pass
    return usersipresp, cardbinresp, cardcountryresp, ipcountryresp


def getbalance(sk):
    try:
        import stripe
        stripe.api_key = sk
        fetch = stripe.Balance.retrieve()
        get = fetch["available"][0]
        currency = fetch["available"][0]["currency"]
        balance = fetch["available"][0]["amount"]
        cards = fetch["available"][0]["source_types"]["card"]
    except:
        currency = "N/A"
        balance = "N/A"
        cards = "N/A"
    return currency, balance, cards

def skmass(sk):
    from FUNC.defs import check_stripe , getsk , getallsk
    try:
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
            response = "SK LIVE ✅"
            resp = f"""
<code>{sk}</code>
<b>Result - {response}</b>
            """
            
        elif "rate limit" in result:
            response = "RATE LIMIT ⚠️"
            resp = f"""
<code>{sk}</code>
<b>Result - {response}</b>
            """
        elif "Invalid API Key" in result:
            response = "Invalid API Key ❌"
        elif "Expired API Key provided" in result:
            response = "Expired API Key ❌"
        elif "Your account cannot currently make live charges." in result:
            response = "Testmode Charges Key ❌"
        else:
            response = "f{result} ❌"
        return (f"<code>{sk}</code>\n<b>Result - {response}</b>\n")
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")