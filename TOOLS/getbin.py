import traceback
import requests
def get_bin_details(cc):
    try:
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
        return "N/A" , "N/A" , "N/A" , "N/A" , "N/A" , "N/A" , "N/A"